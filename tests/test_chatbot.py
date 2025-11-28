import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.chatbot import chatbot

def test_chatbot():
    print("Initializing chatbot...")
    chatbot.initialize()
    
    # Test 1: Semantic Search
    print("\nTest 1: Semantic Search")
    q1 = "como pintar un auto" # Assuming this is in the dataset or similar
    results = chatbot.find_similar(q1)
    if results:
        print(f"Match found for '{q1}': {results[0]['question']} (Score: {results[0]['score']:.2f})")
    else:
        print(f"No match for '{q1}'")

    # Test 2: Keyword Fallback (Typo)
    print("\nTest 2: Keyword Fallback")
    # Assuming 'lijado' is in the dataset, let's try 'lijaddo'
    q2 = "lijaddo" 
    results = chatbot.find_similar(q2)
    if results:
        print(f"Match found for '{q2}': {results[0]['question']} (Score: {results[0]['score']}, Method: {results[0]['method']})")
    else:
        print(f"No match for '{q2}'")

    # Test 3: Context (Mock)
    print("\nTest 3: Context")
    history = [{'role': 'user', 'content': 'pintura roja'}]
    q3 = "y azul?"
    # This won't actually change the result unless we implemented the context logic fully to append text.
    # But we can check if it runs without error.
    results = chatbot.find_similar(q3, history=history)
    print("Context search ran successfully.")

if __name__ == "__main__":
    test_chatbot()
