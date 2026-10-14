from flask import Flask
from flask_jwt_extended import JWTManager

# importamos las dependencias previamente creadas
from app.config import config
from app.extensions import db
from app.services.datos_demo import unsplash


def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
    )

    # cargamos las configuraciones
    app.config.from_object(config)

    # inicializamos la base de datos
    db.init_app(app)

    # inicializamos el JWT
    JWTManager(app)

    # helper para las fotos de ejemplo dentro de las plantillas
    app.add_template_global(unsplash, name="unsplash")

    # manejamos el registro de los blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
