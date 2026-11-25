from app.extensions import db
from app.models.comunes import TimestampMixin


class Premio(TimestampMixin, db.Model):
    __tablename__ = "premios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    entidad_otorgante = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    anio = db.Column(db.Integer, nullable=False, index=True)

    persona_id = db.Column(
        db.Integer,
        db.ForeignKey("personas.id", ondelete="SET NULL"),
        nullable=True,
    )
    proyecto_id = db.Column(
        db.Integer,
        db.ForeignKey("proyectos.id", ondelete="SET NULL"),
        nullable=True,
    )

    persona = db.relationship(
        "Persona",
        backref=db.backref("premios", lazy="dynamic"),
    )
    proyecto = db.relationship(
        "Proyecto",
        backref=db.backref("premios", lazy="dynamic"),
    )

    def __repr__(self) -> str:
        return f"<Premio id={self.id} nombre={self.nombre!r} anio={self.anio}>"
