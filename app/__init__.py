from flask import Flask
from .routes.hello_world_routes import hello_world_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(hello_world_bp)

    return app

if __name__ == '__main__':
    my_app = create_app()
