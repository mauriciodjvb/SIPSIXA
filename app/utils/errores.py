"""Excepciones de negocio. Los servicios las lanzan y un manejador global las
convierte en respuestas JSON con el código HTTP correcto."""


class ErrorServicio(Exception):
    status = 400
    codigo = "Bad Request"

    def __init__(self, mensaje, errores=None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.errores = errores


class NoEncontrado(ErrorServicio):
    status, codigo = 404, "Not Found"


class Conflicto(ErrorServicio):
    status, codigo = 409, "Conflict"


class ReglaNegocio(ErrorServicio):
    status, codigo = 422, "Unprocessable Entity"


class NoAutenticado(ErrorServicio):
    status, codigo = 401, "Unauthorized"


class Prohibido(ErrorServicio):
    status, codigo = 403, "Forbidden"
