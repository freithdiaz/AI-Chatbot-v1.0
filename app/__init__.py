from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from .config import Config

socketio = SocketIO(cors_allowed_origins="*")

def create_app(config_class=Config):
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(config_class)
    
    CORS(app)
    socketio.init_app(app)
    
    # Register blueprints/routes
    from .web.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Initialize events
    from .web import events
    
    return app
