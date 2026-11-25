import enum


class RolUsuario(str, enum.Enum):
    ADMIN = "admin"
    INVESTIGADOR = "investigador"
    COLABORADOR = "colaborador"


class EstadoProyecto(str, enum.Enum):
    BORRADOR = "borrador"
    ACTIVO = "activo"
    FINALIZADO = "finalizado"


class TipoContenido(str, enum.Enum):
    ARTICULO = "articulo"
    NOTICIA = "noticia"
    RECURSO = "recurso"
    GALERIA = "galeria"


class ModalidadEvento(str, enum.Enum):
    PRESENCIAL = "presencial"
    VIRTUAL = "virtual"
    HIBRIDO = "hibrido"


class EstadoInvestigacion(str, enum.Enum):
    EN_CURSO = "en_curso"
    PUBLICADA = "publicada"
    ARCHIVADA = "archivada"