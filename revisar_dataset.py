"""
Script para buscar variaciones específicas en el dataset
"""
import json

def buscar_variaciones():
    # Cargar el dataset actual
    with open("dataset_pintura_mejorado.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)
    
    # Lista de preguntas
    preguntas = [item["question"] for item in dataset]
    
    # Variaciones a buscar
    variaciones = [
        "empresa responsable",
        "quien programó el sistema",
        "autores del sistema",
        "Quién diseñó la máquina",
        "Quién hizo el sistema"
    ]
    
    print(f"Total de preguntas en el dataset: {len(preguntas)}")
    print("\nBuscando variaciones específicas:")
    for variacion in variaciones:
        encontradas = [p for p in preguntas if variacion.lower() in p.lower()]
        if encontradas:
            print(f"✅ '{variacion}' - ENCONTRADA:")
            for e in encontradas:
                print(f"  - {e}")
        else:
            print(f"❌ '{variacion}' - NO ENCONTRADA")
    
    # Verificar por qué no se añaden las variaciones
    print("\nRevisando por qué no se añaden variaciones:")
    # 1. Verificar pregunta original
    original = "¿Quién desarrolló el sistema de pintura?"
    if original in preguntas:
        print(f"Pregunta original '{original}' encontrada en el dataset.")
        # Buscar categoría y respuesta
        for item in dataset:
            if item["question"] == original:
                print(f"Categoría: {item['category']}")
                print(f"Respuesta: {item['answer'][:50]}...")
    else:
        print(f"Pregunta original '{original}' NO encontrada en el dataset.")
    
    # 2. Verificar si las variaciones ya están en el dataset antes de añadirlas
    print("\nSimulando proceso de add_variations:")
    # Crear mapa pregunta -> (respuesta, categoría)
    question_map = {item["question"]: (item["answer"], item["category"]) for item in dataset}
    
    # Verificar si las variaciones ya están en el mapa
    for variacion in variaciones:
        if variacion in question_map:
            print(f"'{variacion}' ya existe en el dataset.")
        else:
            print(f"'{variacion}' no existe en el dataset y debería añadirse.")
    
    # Verificar variaciones específicas solo para preguntas sobre desarrollo
    print("\nRevisando todas las preguntas relacionadas con 'desarrolló' o 'creó':")
    dev_questions = [p for p in preguntas if "desarrolló" in p.lower() or "creó" in p.lower() or "hizo" in p.lower()]
    for q in dev_questions:
        print(f"- {q}")

if __name__ == "__main__":
    buscar_variaciones() 