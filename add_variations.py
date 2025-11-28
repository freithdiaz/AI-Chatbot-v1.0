"""
Script para añadir variaciones de preguntas al dataset
"""
import json

def add_variations():
    # Cargar el dataset actual
    with open("dataset_pintura_mejorado.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)
    
    # Crear un diccionario para buscar respuestas por pregunta
    question_map = {item["question"]: (item["answer"], item["category"]) for item in dataset}
    
    # Definir variaciones de preguntas comunes
    variations = [
        # Variaciones sobre el sistema
        ("¿Qué es el Sistema Automatizado de Pintura?", [
            "Cuéntame sobre el sistema de pintura",
            "Explícame qué hace el sistema de pintura",
            "Para qué sirve la máquina de pintura",
            "Qué es esta máquina de pintura",
            "me puedes decir que es el sistema",
            "sistema de pintura que es",
            "info sobre el sistema de pintura"
        ]),
        # Variaciones sobre modelos
        ("¿Qué modelos se pueden pintar en el sistema?", [
            "Qué puedo pintar con el sistema",
            "Cuáles son los modelos disponibles",
            "Qué equipos puedo pintar",
            "Dime los modelos que soporta",
            "modelos compatibles con el sistema",
            "lista de equipos para pintar",
            "que carcasas puedo pintar"
        ]),
        # Variaciones sobre Kaon
        ("¿Cómo se pinta el modelo Kaon?", [
            "Como pinto un Kaon",
            "Proceso para pintar Kaon",
            "Pasos para pintar un Kaon",
            "Como debo pintar Kaon",
            "pintura de equipos kaon",
            "instrucciones para kaon",
            "kaon procedimiento de pintura"
        ]),
        # Variaciones sobre Opentel
        ("¿Cómo se pinta el modelo Opentel?", [
            "Como pinto un Opentel",
            "Proceso para pintar Opentel",
            "Pasos para pintar un Opentel",
            "Como debo pintar Opentel",
            "opentel como se pinta",
            "pintura de equipo opentel",
            "procedimiento opentel"
        ]),
        # Variaciones sobre Arris
        ("¿Cómo se pinta el modelo Arris?", [
            "Como pinto un Arris",
            "Proceso para pintar Arris",
            "Pasos para pintar un Arris",
            "Como debo pintar Arris",
            "Arris carcasa pintura",
            "pintar un arris",
            "método para pintar arris"
        ]),
        # Variaciones sobre LH
        ("¿Cómo se pinta el modelo LH?", [
            "Como pinto un LH",
            "Proceso para pintar LH",
            "Pasos para pintar un LH",
            "Como debo pintar LH",
            "lh carcasa pintura",
            "pintado de lh",
            "método para pintar lh"
        ]),
        # Variaciones sobre problemas
        ("¿Qué hacer si el sistema no responde?", [
            "El sistema no funciona",
            "La máquina no enciende",
            "Tengo problemas con el sistema",
            "No responde el sistema",
            "Error en el sistema",
            "sistema congelado",
            "fallas en el sistema de pintura"
        ]),
        # Variaciones sobre mantenimiento
        ("¿Qué mantenimiento diario requiere el sistema?", [
            "Como mantener el sistema",
            "Mantenimiento de la máquina",
            "Limpieza del sistema",
            "Cuidados diarios",
            "revisar el sistema",
            "cómo limpiar la máquina",
            "mantenimiento rutinario"
        ]),
        # Variaciones sobre calibración
        ("¿Cómo se calibra la pistola de pintura?", [
            "Calibrar pistola",
            "Ajustar pistola de pintura",
            "Como configurar la pistola",
            "Pasos para calibrar",
            "ajuste de pistola",
            "regular pistola de pintura",
            "configuración de pistola"
        ]),
        # Variaciones sobre componentes
        ("¿Qué componentes principales conforman el sistema?", [
            "Partes del sistema",
            "De qué está hecho el sistema",
            "Elementos del sistema",
            "Componentes de la máquina",
            "piezas del sistema",
            "hardware del sistema",
            "qué tiene el sistema"
        ]),
        # Variaciones sobre inicio
        ("¿Cómo se inicia el sistema correctamente?", [
            "Como encender el sistema",
            "Pasos para iniciar",
            "Como arrancar el sistema",
            "Procedimiento de inicio",
            "como prendo el sistema",
            "iniciar la máquina",
            "encendido del sistema"
        ]),
        # Variaciones sobre creadores
        ("¿Quién desarrolló el sistema de pintura?", [
            "Quién hizo el sistema",
            "Creadores del sistema",
            "Empresa que desarrolló",
            "Quién diseñó la máquina",
            "quien programó el sistema",
            "autores del sistema",
            "empresa responsable"
        ])
    ]
    
    # Añadir variaciones al dataset
    added = 0
    for original, variants in variations:
        if original in question_map:
            answer, category = question_map[original]
            for variant in variants:
                if variant not in question_map:
                    dataset.append({
                        "category": category,
                        "question": variant,
                        "answer": answer
                    })
                    added += 1
    
    # Guardar el dataset actualizado
    with open("dataset_pintura_mejorado.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    
    print(f"Se añadieron {added} variaciones de preguntas al dataset")

if __name__ == "__main__":
    add_variations() 