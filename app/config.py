import os


class config:

    # En Docker, DATABASE_URL llega desde docker-compose (que lee el archivo .env).
    # Si ejecutas la app sin Docker, usa una base SQLite local para poder probar.
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///sipsixa_dev.db"
    )

    # lo usamos para evitar el envio de informacion cuando cambie algun estado
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # clave utilizada para la firma de los tokens (definirla en el .env)
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "solo-para-desarrollo-local")

    # 3600 segundos eso es igual a 1 hora
    JWT_ACCESS_TOKEN_EXPIRES = 3600
