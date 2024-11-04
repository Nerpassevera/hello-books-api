import pytest

def test_get_all_books_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_books_returns_list_of_books(client, two_saved_books):
    # Arrange
    book1 = {
        "id": 1,
        "title":"Ocean Book",
        "description": "watr 4ever"
    }
    book2 = {
        "id": 2,
        "title":"Mountain Book",
        "description": "i luv 2 climb rocs"
    }

    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert all(isinstance(book, dict) for book in response_body)
    assert book1 in response_body
    assert book2 in response_body

def test_get_all_books_returns_filtered_books(client, two_saved_books):
    # Arrange
    filter_query = {"title": "ocean"}
    book1 = {
        "id": 1,
        "title":"Ocean Book",
        "description": "watr 4ever"
    }

    # Act
    response = client.get("/books", query_string = filter_query)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert all(isinstance(book, dict) for book in response_body)
    assert book1 in response_body

def test_get_one_book_missing_record(client, two_saved_books):
    # Act
    response = client.get("/books/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Book with ID 3 not found"}

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4ever"
    }

def test_get_one_book_invalid_id(client, two_saved_books):
    # Act
    response = client.get("/books/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "book id cat is invalid"}

def test_create_one_book(client):
    # Act
    response = client.post("/books", json={
        "title": "New Book",
        "description": "The Best!"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "New Book",
        "description": "The Best!"
    }

def test_create_one_book_no_title(client):
    # Arrange
    test_data = {"description": "The Best!"}

    # Act & Assert
    # with pytest.raises(KeyError, match='title'):
    #     response = client.post("/books", json=test_data)

    # Act
    response = client.post("/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == { "message": "ERROR: Missing the title parameters for creating a book" }


def test_create_one_book_no_description(client):
    # Arrange
    test_data = {"title": "New Book"}

    # # Act & Arrange
    # with pytest.raises(KeyError, match='description'):
    #     response = client.post("/books", json=test_data)

    # Act
    response = client.post("/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == { "message": "ERROR: Missing the description parameters for creating a book" }

def test_create_one_book_with_extra_key(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "title": "New Book",
        "description": "The Best!",
        "another": "last value"
    }

    # Act
    response = client.post("/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "New Book",
        "description": "The Best!",
    }

def test_create_book_with_no_params(client):
    # Arrange
    test_data = {}

    # # Act & Assert
    # with pytest.raises(KeyError, match='title'):
    #     response = client.post("/books", json=test_data)

    # Act
    response = client.post("/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == { "message": "ERROR: No parameters for book has been passed!" }
