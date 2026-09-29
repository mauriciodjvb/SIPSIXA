import os

class config:

    SQLALCHEMY_DATABASE_URI = os.getenv(
       "DATABASE_URL",
       "mysql+pymysql://inventory_user:inventory_password@db:3306/inventory_db" 
    )

    #lo usamos para evitar el envio de informacion cuando cambie algun estado
    SQLALCHEMY_TRACK_NOTIFICATIONS = False

    #clave utilizada para la firma de los tokens
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY", 
        "super-secret-key-produccion"
    )
    #3600 segundos eso es igual a 1 hora
    JWT_ACCESS_TOKEN_EXPIRES = 3600