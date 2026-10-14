from flask import Blueprint, jsonify, render_template
from sqlalchemy import text

from app.extensions import db
from app.services.datos_demo import HALL_FAMA, PROYECTOS

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template(
        "index.html",
        proyectos=PROYECTOS[:3],
        destacados=HALL_FAMA[:4],
    )


# Secciones públicas: por ahora muestran una página "en construcción".
# Se completan en la Parte 3.
@main_bp.route("/historia")
def historia():
    return render_template("en_construccion.html", titulo="Historia del Programa")


@main_bp.route("/premios")
def premios():
    return render_template("en_construccion.html", titulo="Premios y Reconocimientos")


@main_bp.route("/proyectos")
def proyectos():
    return render_template("en_construccion.html", titulo="Proyectos Destacados")


@main_bp.route("/investigacion")
def investigacion():
    return render_template("en_construccion.html", titulo="Investigación")


@main_bp.route("/eventos")
def eventos():
    return render_template("en_construccion.html", titulo="Eventos")


@main_bp.route("/hall-de-la-fama")
def hall_fama():
    return render_template("en_construccion.html", titulo="Hall de la Fama")


@main_bp.route("/login")
def login():
    return render_template("en_construccion.html", titulo="Ingresar")


@main_bp.route("/salud")
def salud():
    """Comprueba que la aplicación web está viva."""
    return jsonify(estado="ok")


@main_bp.route("/salud/db")
def salud_db():
    """Comprueba que la aplicación se puede conectar a la base de datos."""
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify(base_de_datos="conectada")
    except Exception as error:
        return jsonify(base_de_datos="error", detalle=str(error)), 500
