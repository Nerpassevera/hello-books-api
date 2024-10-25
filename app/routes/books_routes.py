from flask import Blueprint

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

# @books_bp.get("/", strict_slashes=False)
# def get_all_books():
#     return [book.to_dict() for book in books]

# # @books_bp.get("/<int:book_id>")
# @books_bp.get("/<book_id>")
# def get_one_book(book_id):
#     book = validate_book(book_id)
#     return book

# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except ValueError:
#         message = {"message": f"book id {book_id} is invalid"}
#         abort(make_response(message, 400))

#     for book in books:
#         if book.id == book_id:
#             return book.to_dict()

#     abort(make_response({ "message": f"Book with ID {book_id} not found"}, 404))
