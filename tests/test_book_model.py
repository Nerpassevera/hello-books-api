from app.models.book import Book
import pytest

def test_from_dict_creates_book_instance():
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    new_book = Book.from_dict(test_data)

    # Arrange
    assert isinstance(new_book, Book)
    assert new_book.title == "New Book"
    assert new_book.description == "The Best!"

def test_from_dict_creates_book_instance_with_extra_keys():
    # Arrange
    test_data = {
        "extra": "some stuff",
        "title": "New Book",
        "description": "The Best!",
        "another": "last value"
    }

    # Act
    new_book = Book.from_dict(test_data)

    # Arrange
    assert isinstance(new_book, Book)
    assert new_book.title == "New Book"
    assert new_book.description == "The Best!"

def test_from_dict_returns_error_to_empty_book():
    # Arrange
    test_data = {}

    # Act & Arrange
    with pytest.raises(KeyError, match='title'):
        new_book = Book.from_dict(test_data)

def test_from_dict_returns_error_to_no_title():
    # Arrange
    test_data = {
        "description": "The Best!"
    }

    # Act & Arrange
    with pytest.raises(KeyError, match='title'):
        new_book = Book.from_dict(test_data)


def test_from_dict_returns_error_to_no_description():
    # Arrange
    test_data = {
        "title": "New Book"
    }

    # Act & Arrange
    with pytest.raises(KeyError, match='description'):
        new_book = Book.from_dict(test_data)
