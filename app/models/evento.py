from app.extensions import db
from app.models.comunes import TimestampMixin
from app.models.constantes import ModalidadEvento


class Evento(TimestampMixin, db.Model):
    __tablename__ = "eventos"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    modalidad = db.Column(
        db.Enum(ModalidadEvento),
        nullable=False,
        default=ModalidadEvento.PRESENCIAL,
    )
    ubicacion_o_enlace = db.Column(db.String(300), nullable=True)
    fecha_inicio = db.Column(db.DateTime, nullable=False, index=True)
    fecha_fin = db.Column(db.DateTime, nullable=True)
    capacidad_maxima = db.Column(db.Integer, nullable=True)

    organizador_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id", ondelete="RESTRICT"),
        nullable=False,
    )
    proyecto_id = db.Column(
        db.Integer,
        db.ForeignKey("proyectos.id", ondelete="SET NULL"),
        nullable=True,
    )

    organizador = db.relationship(
        "Usuario",
        backref=db.backref("eventos_organizados", lazy="dynamic"),
    )
    proyecto = db.relationship(
        "Proyecto",
        backref=db.backref("eventos", lazy="dynamic"),
    )

    def __repr__(self) -> str:
        return f"<Evento id={self.id} titulo={self.titulo!r}>"