from datetime import date

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fecha_larga(valor):
    """'2025-10-15' -> '15 de octubre de 2025'"""
    d = date.fromisoformat(valor)
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"
