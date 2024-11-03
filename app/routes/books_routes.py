from flask import Blueprint, abort, make_response, request, Response
from app.models.book import Book
from app.db import db

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("/", strict_slashes=False)
def create_book():
    request_body = request.get_json()
    new_book = instantiate_book(request_body)
    db.session.add(new_book)
    db.session.commit()

    response = new_book.to_dict()
    return response, 201

def instantiate_book(request_body):
    print(request_body, bool(request_body))

    try:
        title = request_body["title"]
        description = request_body["description"]
        new_book = Book(title=title, description=description)
        return new_book
    except KeyError as mismatch:
        if not request_body:
            message = {"message": "ERROR: No parameters for book has been passed!"}
        else:
            message = {"message": f"ERROR: Missing the {mismatch.args[0]} parameters for creating a book"}
        abort(make_response(message, 400))

@books_bp.get("/", strict_slashes=False)
def get_all_books():
    title_params = request.args.get("title")
    description_params = request.args.get("description")

    query = db.select(Book).order_by(Book.id)

    if title_params:
        query = query.where(Book.title.ilike(f"%{title_params}%"))
    if description_params:
        query = query.where(Book.description.ilike(f"%{description_params}%"))

    books = db.session.scalars(query)
    return [book.to_dict()for book in books]

@books_bp.get("/<book_id>", strict_slashes=False)

def get_one_book(book_id):
    book = validate_book(book_id)
    return book.to_dict()

@books_bp.delete("/<book_id>", strict_slashes=False)
def delete_a_book(book_id):
    book = validate_book(book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except ValueError:
        message = {"message": f"book id {book_id} is invalid"}
        abort(make_response(message, 400))

    query = db.select(Book).where(Book.id == book_id)
    book = db.session.scalar(query)

    if not book:
        abort(make_response({ "message": f"Book with ID {book_id} not found"}, 404))

    return book

@books_bp.put("/<book_id>", strict_slashes=False)
def edit_a_book(book_id):
    book = validate_book(book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()
    return Response(status=204, mimetype="application/json")
