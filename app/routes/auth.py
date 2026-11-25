from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from marshmallow import EXCLUDE, Schema, ValidationError, fields, validate
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models.constantes import RolUsuario
from app.models.persona import Persona
from app.models.usuario import Usuario
from app.utils.seguridad import roles_required

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


class RegistroSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    correo = fields.Email(required=True)
    clave = fields.String(required=True, validate=validate.Length(min=8, max=128))
    nombre = fields.String(required=False, validate=validate.Length(min=2, max=240))
    nombres = fields.String(required=False, validate=validate.Length(min=2, max=120))
    apellidos = fields.String(required=False, validate=validate.Length(min=2, max=120))
    rol = fields.String(required=False, load_default=RolUsuario.COLABORADOR.value)


class LoginSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    correo = fields.Email(required=True)
    clave = fields.String(required=True, load_only=True)


registro_schema = RegistroSchema()
login_schema = LoginSchema()


def _separar_nombre_completo(nombre_completo: str | None) -> tuple[str, str]:
    limpio = ' '.join((nombre_completo or '').strip().split())
    if not limpio:
        return 'Usuario', 'SIPSIXA'
    partes = limpio.split(' ', 1)
    if len(partes) == 1:
        return partes[0], 'SIPSIXA'
    return partes[0], partes[1]


@auth_bp.route('/registro', methods=['POST'])
def registro():
    payload = request.get_json(silent=True) or {}
    try:
        datos = registro_schema.load(payload)
    except ValidationError as err:
        return jsonify(error='Datos de registro inválidos', detalles=err.messages), 400

    correo = datos['correo'].strip().lower()
    if Usuario.query.filter_by(correo=correo).first():
        return jsonify(error='El correo ya está registrado'), 409

    rol_solicitado = str(datos.get('rol') or RolUsuario.COLABORADOR.value).strip().lower()
    try:
        rol_enum = RolUsuario(rol_solicitado)
    except ValueError:
        return (
            jsonify(
                error='Rol inválido',
                roles_permitidos=[RolUsuario.COLABORADOR.value, RolUsuario.INVESTIGADOR.value],
            ),
            400,
        )

    if rol_enum == RolUsuario.ADMIN:
        return jsonify(error='No está permitido auto-registrarse con rol administrador'), 403

    nombres = (datos.get('nombres') or '').strip()
    apellidos = (datos.get('apellidos') or '').strip()
    if not nombres or not apellidos:
        nom_calc, ape_calc = _separar_nombre_completo(datos.get('nombre'))
        nombres = nombres or nom_calc
        apellidos = apellidos or ape_calc

    usuario = Usuario(correo=correo, rol=rol_enum, activo=True)
    usuario.set_password(datos['clave'])

    persona = Persona(
        nombres=nombres,
        apellidos=apellidos,
        usuario=usuario,
    )

    try:
        db.session.add(usuario)
        db.session.add(persona)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(error='No se pudo completar el registro por conflicto de datos'), 409

    token = create_access_token(
        identity=str(usuario.id),
        additional_claims={'rol': usuario.rol.value},
    )
    return (
        jsonify(
            mensaje='Usuario registrado exitosamente',
            access_token=token,
            usuario=usuario.to_dict(),
        ),
        201,
    )


@auth_bp.route('/login', methods=['POST'])
def login():
    payload = request.get_json(silent=True) or {}
    try:
        datos = login_schema.load(payload)
    except ValidationError as err:
        return jsonify(error='Datos de inicio de sesión inválidos', detalles=err.messages), 400

    correo = datos['correo'].strip().lower()
    usuario = Usuario.query.filter_by(correo=correo).first()

    if usuario is None or not usuario.check_password(datos['clave']):
        return jsonify(error='Correo o contraseña incorrectos'), 401

    if not usuario.activo:
        return jsonify(error='La cuenta de usuario está inactiva'), 403

    token = create_access_token(
        identity=str(usuario.id),
        additional_claims={'rol': usuario.rol.value},
    )
    return (
        jsonify(
            mensaje='Inicio de sesión exitoso',
            access_token=token,
            usuario=usuario.to_dict(),
        ),
        200,
    )


@auth_bp.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    identidad = get_jwt_identity()
    try:
        usuario_id = int(identidad)
    except (TypeError, ValueError):
        return jsonify(error='Token inválido'), 401

    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        return jsonify(error='Usuario no encontrado'), 404

    return jsonify(usuario=usuario.to_dict()), 200


@auth_bp.route('/admin/chequeo', methods=['GET'])
@roles_required(RolUsuario.ADMIN)
def admin_chequeo():
    return jsonify(mensaje='Acceso autorizado para administrador'), 200
