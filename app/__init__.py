from flask import Flask
from app.routes.books_routes import books_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(books_bp)

    return app

if __name__ == '__main__':
    my_app = create_app()
