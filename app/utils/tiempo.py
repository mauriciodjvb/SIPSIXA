from datetime import datetime, timezone


def ahora():
    """Fecha y hora UTC sin zona horaria (así se guarda en MySQL)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)
