from flash import flask
from flash_jwk_extended import jwtManager

#importamos las diferencia previamentes creadas 
from app.config import config
from app.extensions import db

#manjeos de rutas con blueprint


#
def create_app():

    app = flask(
__name__,
static_folder = "static",
template_folder = "templates"
    )
    #cargamos las configuraciones
    app.config.from_object(config)
    #inicializamos
    db.init_app(app)
#inicializamos el JWT
    jwtManager(app)



    #manejamos el registro del blueprint

    with app.app_context():
        db.create_all()
    return app