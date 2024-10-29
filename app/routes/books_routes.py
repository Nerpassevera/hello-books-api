from flask import Blueprint, abort, make_response, request, Response
from app.models.book import Book
from app.db import db

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("/", strict_slashes=False)
def create_book():
    request_body = request.get_json()
    title = request_body["title"]
    description = request_body["description"]

    new_book = Book(title=title, description=description)
    db.session.add(new_book)
    db.session.commit()

    response = new_book.to_dict()
    return response, 201

@books_bp.get("/", strict_slashes=False)
def get_all_books():
    query = db.select(Book).order_by(Book.id)
    books = db.session.scalars(query)
    return [book.to_dict()for book in books]

@books_bp.get("/<book_id>", strict_slashes=False)

def get_one_book(book_id):
    book = validate_book(book_id)
    return book.to_dict()

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except ValueError:
        message = {"message": f"book id {book_id} is invalid"}
        abort(make_response(message, 400))

    query = db.select(Book).where(Book.id == book_id)
    book = db.session.scalar(query)

    if book:
        return book

    abort(make_response({ "message": f"Book with ID {book_id} not found"}, 404))

@books_bp.put("/<book_id>", strict_slashes=False)
def edit_a_book(book_id):
    book = validate_book(book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()
    return Response(status=204, mimetype="application/json")
