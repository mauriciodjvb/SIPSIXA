from app.extensions import db
from app.models.comunes import TimestampMixin
from app.models.constantes import EstadoProyecto

proyecto_participantes = db.Table(
    "proyecto_participantes",
    db.Column(
        "proyecto_id",
        db.Integer,
        db.ForeignKey("proyectos.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    db.Column(
        "persona_id",
        db.Integer,
        db.ForeignKey("personas.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Proyecto(TimestampMixin, db.Model):
    __tablename__ = "proyectos"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(180), nullable=False)
    resumen = db.Column(db.Text, nullable=True)
    estado = db.Column(
        db.Enum(EstadoProyecto),
        nullable=False,
        default=EstadoProyecto.BORRADOR,
    )
    creador_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id", ondelete="RESTRICT"),
        nullable=False,
    )

    creador = db.relationship("Usuario", back_populates="proyectos_creados")
    participantes = db.relationship(
        "Persona",
        secondary=proyecto_participantes,
        backref=db.backref("proyectos", lazy="dynamic"),
    )

    def __repr__(self) -> str:
        return f"<Proyecto id={self.id} titulo={self.titulo!r}>"
