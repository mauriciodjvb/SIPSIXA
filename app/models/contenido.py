from app.extensions import db
from app.models.comunes import TimestampMixin
from app.models.constantes import TipoContenido


class Contenido(TimestampMixin, db.Model):
    __tablename__ = "contenidos"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(220), unique=True, nullable=False, index=True)
    resumen = db.Column(db.Text, nullable=True)
    cuerpo = db.Column(db.Text, nullable=False)
    tipo = db.Column(
        db.Enum(TipoContenido),
        nullable=False,
        default=TipoContenido.ARTICULO,
    )
    url_imagen = db.Column(db.String(500), nullable=True)
    publicado = db.Column(db.Boolean, nullable=False, default=False)

    autor_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id", ondelete="RESTRICT"),
        nullable=False,
    )
    proyecto_id = db.Column(
        db.Integer,
        db.ForeignKey("proyectos.id", ondelete="SET NULL"),
        nullable=True,
    )

    autor = db.relationship("Usuario", backref=db.backref("contenidos", lazy="dynamic"))
    proyecto = db.relationship(
        "Proyecto",
        backref=db.backref("contenidos", lazy="dynamic"),
    )

    def __repr__(self) -> str:
        return f"<Contenido id={self.id} slug={self.slug!r}>"
