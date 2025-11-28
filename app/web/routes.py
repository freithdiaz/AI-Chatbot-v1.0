from flask import Blueprint, render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os

main_bp = Blueprint('main', __name__)

@main_bp.route("/Chat")
def index():
    return render_template("index.html")

@main_bp.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"response": "No se envió ningún archivo."}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"response": "Nombre de archivo vacío."}), 400
    
    if file:
        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, filename))
        return jsonify({"response": f"Archivo '{filename}' subido correctamente."})
    
    return jsonify({"response": "Error al subir archivo."}), 400
