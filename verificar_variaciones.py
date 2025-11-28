"""
Script para verificar la existencia de preguntas en el dataset
"""
import json

def verificar_preguntas():
    # Cargar el dataset actual
    with open("dataset_pintura_mejorado.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)
    
    # Crear una lista de todas las preguntas en el dataset
    preguntas = [item["question"] for item in dataset]
    
    # Preguntas originales a verificar
    originales = [
        "¿Qué es el Sistema Automatizado de Pintura?",
        "¿Qué modelos se pueden pintar en el sistema?",
        "¿Cómo se pinta el modelo Kaon?",
        "¿Cómo se pinta el modelo Opentel?",
        "¿Cómo se pinta el modelo Arris?",
        "¿Cómo se pinta el modelo LH?",
        "¿Qué hacer si el sistema no responde?",
        "¿Qué mantenimiento diario requiere el sistema?",
        "¿Cómo se calibra la pistola de pintura?",
        "¿Qué componentes principales conforman el sistema?",
        "¿Cómo se inicia el sistema correctamente?",
        "¿Quién desarrolló el sistema de pintura?"
    ]
    
    print("Estado de las preguntas originales:")
    for pregunta in originales:
        if pregunta in preguntas:
            print(f"✅ '{pregunta}' - ENCONTRADA")
        else:
            print(f"❌ '{pregunta}' - NO ENCONTRADA")
    
    print("\nBuscando preguntas similares para las no encontradas:")
    for pregunta in originales:
        if pregunta not in preguntas:
            similares = [p for p in preguntas if pregunta.lower() in p.lower()]
            print(f"Para '{pregunta}', encontré estas similares:")
            for similar in similares:
                print(f"  - {similar}")

if __name__ == "__main__":
    verificar_preguntas() 