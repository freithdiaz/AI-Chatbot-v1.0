import json
import os
from ..config import Config

class DataManager:
    def __init__(self):
        self.dataset_path = Config.DATASET_FILE
        self.questions = []
        self.answers = []
        self.categories = []

    def load_data(self):
        if not os.path.exists(self.dataset_path):
            return False, "Dataset file not found."
        
        try:
            with open(self.dataset_path, "r", encoding="utf-8") as f:
                dataset = json.load(f)
            
            self.questions = [item["question"] for item in dataset]
            self.answers = [item["answer"] for item in dataset]
            self.categories = [item["category"] for item in dataset]
            return True, f"Loaded {len(self.questions)} items."
        except Exception as e:
            return False, str(e)

    def save_question_answer(self, question, answer):
        try:
            with open(self.dataset_path, "r", encoding="utf-8") as f:
                dataset = json.load(f)
            
            dataset.append({
                "category": "nuevo",
                "question": question,
                "answer": answer
            })
            
            with open(self.dataset_path, "w", encoding="utf-8") as f:
                json.dump(dataset, f, ensure_ascii=False, indent=2)
            
            # Reload data in memory
            self.load_data()
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    def get_data(self):
        return self.questions, self.answers, self.categories
