from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db
from app.models.comunes import TimestampMixin
from app.models.constantes import RolUsuario


class Usuario(TimestampMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(
        db.Enum(RolUsuario),
        nullable=False,
        default=RolUsuario.COLABORADOR,
    )
    activo = db.Column(db.Boolean, nullable=False, default=True)

    persona = db.relationship(
        "Persona",
        back_populates="usuario",
        uselist=False,
        cascade="all, delete-orphan",
    )

    proyectos_creados = db.relationship(
        "Proyecto",
        back_populates="creador",
        lazy="dynamic",
    )

    def set_password(self, clave: str) -> None:
        self.password_hash = generate_password_hash(clave)

    def check_password(self, clave: str) -> bool:
        if not clave or not self.password_hash:
            return False
        return check_password_hash(self.password_hash, clave)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "correo": self.correo,
            "rol": self.rol.value if isinstance(self.rol, RolUsuario) else str(self.rol),
            "activo": self.activo,
            "persona": (
                {
                    "id": self.persona.id,
                    "nombres": self.persona.nombres,
                    "apellidos": self.persona.apellidos,
                    "biografia": self.persona.biografia,
                }
                if self.persona
                else None
            ),
        }

    def __repr__(self) -> str:
        return f"<Usuario id={self.id} correo={self.correo!r}>"