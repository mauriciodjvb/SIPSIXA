from flask import Flask
from flask_jwt_extended import JWTManager

from app.config import config
from app.extensions import db
from app.services.datos_demo import semilla_contenidos, unsplash
from app.services.formato import fecha_larga


def create_app(*args, **kwargs):
    flask_app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
    )

    flask_app.config.from_object(config)

    db.init_app(flask_app)
    JWTManager(flask_app)

    flask_app.add_template_global(unsplash, name="unsplash")
    flask_app.add_template_filter(fecha_larga, name="fecha_larga")
    flask_app.add_template_global(semilla_contenidos, name="semilla_contenidos")

    from app.routes import auth_bp, main_bp
    flask_app.register_blueprint(main_bp)
    flask_app.register_blueprint(auth_bp)

    with flask_app.app_context():
        import app.models
        db.create_all()

    return flask_app
