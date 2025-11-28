from sentence_transformers import SentenceTransformer, util
import torch
import re
from .data_manager import DataManager
from ..config import Config

class Chatbot:
    def __init__(self):
        self.model = None
        self.embeddings = None
        self.data_manager = DataManager()
        self.is_ready = False

    def initialize(self):
        print("Loading model...")
        try:
            self.model = SentenceTransformer(Config.MODEL_NAME)
            success, msg = self.data_manager.load_data()
            if success:
                self.update_embeddings()
                self.is_ready = True
                print(msg)
            else:
                print(f"Failed to load data: {msg}")
        except Exception as e:
            print(f"Error initializing chatbot: {e}")

    def update_embeddings(self):
        questions, _, _ = self.data_manager.get_data()
        if questions:
            print("Generating embeddings...")
            self.embeddings = self.model.encode(questions, convert_to_tensor=True)

    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-záéíóúüñ0-9\s]', '', text)
        text = ' '.join(text.split())
        return text

    def find_similar(self, user_question, threshold=0.65, history=None):
        if not self.is_ready:
            return []

        # 1. Semantic Search
        processed_question = self.preprocess_text(user_question)
        
        # Context enhancement (simple)
        if history and len(history) > 0:
            last_msg = history[-1]
            if len(user_question.split()) < 3 and last_msg['role'] == 'user':
                # If query is very short, maybe it refers to previous context
                # For now, we just log it, but we could append it.
                # processed_question = f"{last_msg['content']} {processed_question}"
                pass

        user_embedding = self.model.encode(processed_question, convert_to_tensor=True)
        
        scores = util.cos_sim(user_embedding, self.embeddings)[0]
        
        top_k = 5
        top_indices = torch.topk(scores, k=min(top_k, len(scores))).indices.tolist()
        top_scores = scores[top_indices].tolist()
        
        questions, answers, categories = self.data_manager.get_data()
        
        similar_questions = []
        for idx, score in zip(top_indices, top_scores):
            if score >= threshold:
                similar_questions.append({
                    "question": questions[idx],
                    "answer": answers[idx],
                    "category": categories[idx],
                    "score": score,
                    "method": "semantic"
                })
        
        # 2. Keyword Fallback (if no good semantic matches)
        if not similar_questions:
            print("Low semantic confidence, trying keyword search...")
            from difflib import get_close_matches
            
            # Simple keyword matching
            matches = get_close_matches(user_question, questions, n=3, cutoff=0.4)
            for match in matches:
                idx = questions.index(match)
                similar_questions.append({
                    "question": questions[idx],
                    "answer": answers[idx],
                    "category": categories[idx],
                    "score": 0.5, # Artificial score
                    "method": "keyword"
                })

        return similar_questions

    def learn_new_answer(self, question, answer):
        success = self.data_manager.save_question_answer(question, answer)
        if success:
            self.update_embeddings()
        return success

    def get_related_questions(self, category, exclude_question):
        questions, _, categories = self.data_manager.get_data()
        related = []
        for i, q in enumerate(questions):
            if categories[i] == category and q != exclude_question:
                related.append(q)
        return related

# Global instance
chatbot = Chatbot()
