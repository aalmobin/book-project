import pytest
from django.urls import reverse

from core.models import Author, Book


@pytest.mark.django_db
def test_register_user(api_client):
    data = {
        "username": "testuser",
        "password": "xcvpassword123",
        "password2": "xcvpassword123",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
    }
    response = api_client.post(reverse("register-user"), data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_book_list(authenticated_client, book_fixture):
    response = authenticated_client.get("/api/v1/books/")
    assert Book.objects.all().count() == 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_book_details(authenticated_client, book_fixture):
    response = authenticated_client.get(f"/api/v1/books/{book_fixture.id}/")
    assert response.status_code == 200
    assert response.data["id"] == book_fixture.id


@pytest.mark.django_db
def test_book_create(authenticated_client, author_fixture):
    data = {
        "title": "New book",
        "author": author_fixture.id,
        "published_at": "1813-01-28",
        "genre": "Comedy",
        "is_archived": False,
    }
    response = authenticated_client.post("/api/v1/books/", data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_book_update(authenticated_client, book_fixture):
    data = {
        "title": "Updated title",
    }
    response = authenticated_client.patch(f"/api/v1/books/{book_fixture.id}/", data)
    assert response.status_code == 200
    assert response.data["title"] == "Updated title"


@pytest.mark.django_db
def test_book_delete(authenticated_client, book_fixture):
    response = authenticated_client.delete(f"/api/v1/books/{book_fixture.id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_author_list(authenticated_client, author_fixture):
    response = authenticated_client.get("/api/v1/authors/")
    assert Author.objects.all().count() == 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_author_details(authenticated_client, author_fixture):
    response = authenticated_client.get(f"/api/v1/authors/{author_fixture.id}/")
    assert response.status_code == 200
    assert response.data["id"] == author_fixture.id


@pytest.mark.django_db
def test_author_create(authenticated_client):
    data = {"name": "Jane Austen", "date_of_birth": "1775-12-16"}
    response = authenticated_client.post("/api/v1/authors/", data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_book_update(authenticated_client, author_fixture):
    data = {
        "name": "Updated Name",
    }
    response = authenticated_client.patch(f"/api/v1/authors/{author_fixture.id}/", data)
    assert response.status_code == 200
    assert response.data["name"] == "Updated Name"


@pytest.mark.django_db
def test_book_delete(authenticated_client, author_fixture):
    response = authenticated_client.delete(f"/api/v1/authors/{author_fixture.id}/")
    assert response.status_code == 204
