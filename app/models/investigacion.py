from app.extensions import db
from app.models.comunes import TimestampMixin
from app.models.constantes import EstadoInvestigacion

investigacion_autores = db.Table(
    "investigacion_autores",
    db.Column(
        "investigacion_id",
        db.Integer,
        db.ForeignKey("investigaciones.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    db.Column(
        "persona_id",
        db.Integer,
        db.ForeignKey("personas.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Investigacion(TimestampMixin, db.Model):
    __tablename__ = "investigaciones"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(220), nullable=False)
    resumen = db.Column(db.Text, nullable=True)
    linea_investigacion = db.Column(db.String(150), nullable=True)
    estado = db.Column(
        db.Enum(EstadoInvestigacion),
        nullable=False,
        default=EstadoInvestigacion.EN_CURSO,
    )
    anio_publicacion = db.Column(db.Integer, nullable=True)
    url_documento = db.Column(db.String(500), nullable=True)

    lider_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id", ondelete="RESTRICT"),
        nullable=False,
    )
    proyecto_id = db.Column(
        db.Integer,
        db.ForeignKey("proyectos.id", ondelete="SET NULL"),
        nullable=True,
    )

    lider = db.relationship(
        "Usuario",
        backref=db.backref("investigaciones_lideradas", lazy="dynamic"),
    )
    proyecto = db.relationship(
        "Proyecto",
        backref=db.backref("investigaciones", lazy="dynamic"),
    )
    autores = db.relationship(
        "Persona",
        secondary=investigacion_autores,
        backref=db.backref("investigaciones", lazy="dynamic"),
    )

    def __repr__(self) -> str:
        return f"<Investigacion id={self.id} titulo={self.titulo!r}>"
