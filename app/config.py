import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = 'uploads'
    DATASET_FILE = 'dataset_pintura_mejorado.json'
    MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
