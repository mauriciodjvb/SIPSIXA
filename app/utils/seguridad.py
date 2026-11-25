from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from app.models.constantes import RolUsuario
from app.models.usuario import Usuario


def roles_required(*roles_permitidos: RolUsuario):
    """Restringe el acceso a usuarios autenticados con alguno de los roles indicados."""

    roles_set = {
        r if isinstance(r, RolUsuario) else RolUsuario(str(r).lower())
        for r in roles_permitidos
    }

    def decorador(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            identidad = get_jwt_identity()

            try:
                usuario_id = int(identidad)
            except (TypeError, ValueError):
                return jsonify(error="Token de acceso inválido"), 401

            usuario = Usuario.query.get(usuario_id)
            if usuario is None:
                return jsonify(error="Usuario no encontrado"), 401

            if not usuario.activo:
                return jsonify(error="La cuenta de usuario está inactiva"), 403

            if roles_set and usuario.rol not in roles_set:
                return (
                    jsonify(
                        error="No tienes permisos suficientes para esta acción",
                        rol_actual=usuario.rol.value,
                        roles_permitidos=[r.value for r in roles_set],
                    ),
                    403,
                )

            return fn(*args, **kwargs)

        return wrapper

    return decorador