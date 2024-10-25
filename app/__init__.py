from flask import Flask
from .db import db, migrate
from .models import book
from .routes.books_routes import books_bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgresql_admin@localhost:5432/hello_books_development'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(books_bp)

    return app

if __name__ == '__main__':
    my_app = create_app()
