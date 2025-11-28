from flask_socketio import send
from .. import socketio
from ..core.chatbot import chatbot
import random
import traceback
from collections import deque

# Global state for conversation context
# In a production app with multiple users, this should be session-based or database-backed
pending_question = None
conversation_history = deque(maxlen=5)

@socketio.on("message")
def handle_message(message):
    global pending_question
    
    try:
        # Initialize chatbot if not ready (lazy loading)
        if not chatbot.is_ready:
            chatbot.initialize()

        # Check if it's an answer to a pending question
        if message.startswith("respuesta:") and pending_question:
            answer = message.replace("respuesta:", "").strip()
            chatbot.learn_new_answer(pending_question, answer)
            pending_question = None
            response = "¡Gracias! He guardado tu respuesta en el dataset."
            
            # Add to history
            conversation_history.append({"role": "user", "content": message})
            conversation_history.append({"role": "bot", "content": response})
        else:
            # Search for similar questions with history context
            similar_questions = chatbot.find_similar(message, history=list(conversation_history))
            
            if similar_questions:
                best_match = similar_questions[0]
                current_category = best_match['category']
                
                response = best_match['answer']
                response += f"\n\nCategoría: {current_category}"
                
                # Get related questions
                related = chatbot.get_related_questions(current_category, best_match['question'])
                if related:
                    response += "\n\n¿Quizás también te interese saber sobre:\n"
                    selected = random.sample(related, min(3, len(related)))
                    for q in selected:
                        response += f"- {q}\n"
            else:
                pending_question = message
                response = (
                    "🤔 No estoy seguro de haber entendido tu pregunta.\n\n"
                    "¿Te gustaría proporcionar una respuesta para esta pregunta?\n"
                    "Si es así, responde con: respuesta:tu respuesta\n\n"
                    f"Pregunta: {message}"
                )
        
        # Update history
        conversation_history.append({"role": "user", "content": message})
        conversation_history.append({"role": "bot", "content": response})
        
    except Exception as e:
        print(f"Error processing message: {e}")
        traceback.print_exc()
        response = "Lo siento, ocurrió un error al procesar tu pregunta."
    
    send(response)
