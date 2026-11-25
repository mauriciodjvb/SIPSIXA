import os

from app import create_app

_flask_app = create_app()
application = _flask_app
app = _flask_app


def wsgi_app(environ, start_response):
    return _flask_app.wsgi_app(environ, start_response)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=os.getenv("FLASK_DEBUG") == "1",
    )
