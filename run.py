import os

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Solo para ejecutar sin Docker. En Docker se usa gunicorn.
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=os.getenv("FLASK_DEBUG") == "1",
    )
