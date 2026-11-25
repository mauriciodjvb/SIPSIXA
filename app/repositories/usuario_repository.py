from typing import Optional, List
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from app.models.usuario import Usuario


class UsuarioRepository:
    @staticmethod
    def obtener_todos() -> List[Usuario]:
        return Usuario.query.order_by(Usuario.id.asc()).all()

    @staticmethod
    def obtener_por_id(usuario_id: int) -> Optional[Usuario]:
        return db.session.get(Usuario, usuario_id)

    @staticmethod
    def obtener_por_correo(correo: str) -> Optional[Usuario]:
        return Usuario.query.filter_by(correo=correo.strip().lower()).first()

    @staticmethod
    def crear(nombre: str, correo: str, password: str, rol: str = "usuario") -> Usuario:
        usuario = Usuario(
            nombre=nombre.strip(),
            correo=correo.strip().lower(),
            rol=rol.strip().lower(),
        )
        usuario.set_password(password)
        try:
            db.session.add(usuario)
            db.session.commit()
            return usuario
        except SQLAlchemyError as error:
            db.session.rollback()
            raise error

    @staticmethod
    def actualizar(usuario: Usuario, datos: dict) -> Usuario:
        if "nombre" in datos and datos["nombre"] is not None:
            usuario.nombre = datos["nombre"].strip()
        if "correo" in datos and datos["correo"] is not None:
            usuario.correo = datos["correo"].strip().lower()
        if "rol" in datos and datos["rol"] is not None:
            usuario.rol = datos["rol"].strip().lower()
        if "activo" in datos and datos["activo"] is not None:
            usuario.activo = bool(datos["activo"])
        if "password" in datos and datos["password"]:
            usuario.set_password(datos["password"])

        try:
            db.session.commit()
            return usuario
        except SQLAlchemyError as error:
            db.session.rollback()
            raise error

    @staticmethod
    def eliminar(usuario: Usuario) -> None:
        try:
            db.session.delete(usuario)
            db.session.commit()
        except SQLAlchemyError as error:
            db.session.rollback()
            raise error