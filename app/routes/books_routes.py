from flask import Blueprint
from app.models.books import books

books_bp = Blueprint("books_bp", __name__, url_prefix="/books/")

@books_bp.get("", strict_slashes=True)
def get_all_books():
    return [book.to_dict() for book in books]
