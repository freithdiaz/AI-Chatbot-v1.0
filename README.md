# 🎨 AI Art Chatbot

> Un asistente inteligente experto en arte, potenciado por embeddings y búsqueda semántica.

Este proyecto implementa un chatbot capaz de responder preguntas sobre arte y pintura utilizando un modelo de lenguaje (Sentence Transformers) para entender el contexto y la semántica de las preguntas del usuario, ofreciendo respuestas precisas desde un dataset curado.

## ✨ Características

- **🧠 Búsqueda Semántica**: Utiliza `sentence-transformers/all-mpnet-base-v2` para entender el significado de las preguntas, no solo palabras clave.
- **⚡ Comunicación en Tiempo Real**: Implementado con WebSockets (Flask-SocketIO) para una experiencia de chat fluida.
- **🔄 Aprendizaje Continuo**: Capacidad para aprender nuevas respuestas y expandir su base de conocimiento dinámicamente.
- **📂 Estructura Modular**: Arquitectura limpia y escalable, separando lógica de negocio, datos y presentación.
- **🖼️ Interfaz Amigable**: Diseño web limpio y responsivo.

## 🚀 Instalación y Uso

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos

1.  **Clonar el repositorio**
    ```bash
    git clone <tu-repositorio-url>
    cd chatbot
    ```

2.  **Crear un entorno virtual** (Recomendado)
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la aplicación**
    ```bash
    python run.py
    ```
    La primera vez que se ejecute, el sistema descargará el modelo de lenguaje (aprox. 400MB), por lo que puede tardar unos momentos.

5.  **Acceder al Chatbot**
    Abre tu navegador y visita: `http://localhost:5000`

## 📁 Estructura del Proyecto

```
chatbot/
├── app/                 # Código fuente principal
│   ├── core/            # Lógica del chatbot y manejo de datos
│   ├── web/             # Rutas y eventos web (Flask/SocketIO)
│   └── __init__.py      # Factory de la aplicación
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── templates/           # Plantillas HTML
├── run.py               # Punto de entrada de la aplicación
├── requirements.txt     # Dependencias del proyecto
└── dataset_*.json       # Base de conocimiento del chatbot
```

## 🛠️ Tecnologías

- **Backend**: Flask, Flask-SocketIO
- **IA/ML**: Sentence-Transformers, PyTorch, scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript (Socket.IO client)

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor lee [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles sobre cómo colaborar en este proyecto.
