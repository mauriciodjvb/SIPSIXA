from app.extensions import db
from app.models.comunes import TimestampMixin


class Persona(TimestampMixin, db.Model):
    __tablename__ = "personas"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )
    nombres = db.Column(db.String(120), nullable=False)
    apellidos = db.Column(db.String(120), nullable=False)
    biografia = db.Column(db.Text, nullable=True)

    usuario = db.relationship("Usuario", back_populates="persona")

    def __repr__(self) -> str:
        return f"<Persona id={self.id} nombre={self.nombres!r}>"
