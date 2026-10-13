from flask import Flask
from flask_jwt_extended import JWTManager

# Importamos las configuraciones y extensiones
from app.config import config
from app.extensions import db

# IMPORTANTE: Importamos el modelo para que la base de datos lo cree automáticamente
from app.models import Producto

def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates"
    )
    
    # Cargamos las configuraciones
    app.config.from_object(config)
    
    # Inicializamos la base de datos y JWT
    db.init_app(app)
    jwt = JWTManager(app)

    # Creamos las tablas en la base de datos dentro del contexto de la app
    with app.app_context():
        db.create_all()
        
    return app