from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la Base de Datos MySQL usando el contenedor 'SIPSIXA_db'
    # Cambia 'tu_usuario', 'tu_contraseña' y 'tu_base_de_datos' según tus credenciales de Docker/MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tu_contraseña@SIPSIXA_db/tu_base_de_datos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registrar rutas o blueprints aquí
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app