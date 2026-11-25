from app.extensions import db
from app.models.comunes import TimestampMixin


class Historia(TimestampMixin, db.Model):
    __tablename__ = "historias"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    relato = db.Column(db.Text, nullable=False)
    fecha_suceso = db.Column(db.Date, nullable=True, index=True)
    destacada = db.Column(db.Boolean, nullable=False, default=False)

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
        backref=db.backref("historias", lazy="dynamic"),
    )
    proyecto = db.relationship(
        "Proyecto",
        backref=db.backref("historias", lazy="dynamic"),
    )

    def __repr__(self) -> str:
        return f"<Historia id={self.id} titulo={self.titulo!r}>"