from app import create_app, socketio
from app.core.chatbot import chatbot

app = create_app()

if __name__ == "__main__":
    print("Starting Chatbot Application...")
    # Pre-load the model
    chatbot.initialize()
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
