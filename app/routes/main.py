from flask import Blueprint, abort, jsonify, render_template
from sqlalchemy import text

from app.extensions import db
from app.services.datos_demo import (
    EVENTOS, GALERIA_EVENTO, GALERIA_HISTORIA, HALL_FAMA, INVESTIGACION,
    LINEA_TIEMPO, PREMIOS, PROYECTOS, buscar,
)

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template(
        "index.html",
        proyectos=PROYECTOS[:3],
        destacados=HALL_FAMA[:4],
    )


# ---------- Secciones públicas ----------
@main_bp.route("/historia")
def historia():
    return render_template("historia.html", linea=LINEA_TIEMPO, galeria=GALERIA_HISTORIA)


@main_bp.route("/premios")
def premios():
    return render_template("premios.html", premios=PREMIOS)


@main_bp.route("/proyectos")
def proyectos():
    anios = sorted({str(p["anio"]) for p in PROYECTOS})
    return render_template("proyectos.html", proyectos=PROYECTOS, anios=anios)


@main_bp.route("/proyectos/<int:proyecto_id>")
def proyecto_detalle(proyecto_id):
    proyecto = buscar(PROYECTOS, proyecto_id)
    if proyecto is None:
        abort(404)
    return render_template("proyecto_detalle.html", proyecto=proyecto)


@main_bp.route("/investigacion")
def investigacion():
    return render_template("investigacion.html", grupos=INVESTIGACION)


@main_bp.route("/eventos")
def eventos():
    proximos = sorted((e for e in EVENTOS if e["tipo"] == "proximo"), key=lambda e: e["fecha"])
    realizados = sorted((e for e in EVENTOS if e["tipo"] == "realizado"), key=lambda e: e["fecha"], reverse=True)
    return render_template("eventos.html", eventos=proximos + realizados)


@main_bp.route("/eventos/<int:evento_id>")
def evento_detalle(evento_id):
    evento = buscar(EVENTOS, evento_id)
    if evento is None:
        abort(404)
    return render_template("evento_detalle.html", evento=evento, galeria=GALERIA_EVENTO)


@main_bp.route("/hall-de-la-fama")
def hall_fama():
    return render_template("hall_fama.html", personas=HALL_FAMA)


@main_bp.route("/hall-de-la-fama/<int:persona_id>")
def perfil(persona_id):
    persona = buscar(HALL_FAMA, persona_id)
    if persona is None:
        abort(404)
    return render_template("perfil.html", persona=persona)


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
