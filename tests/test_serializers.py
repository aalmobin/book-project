import pytest
from rest_framework.exceptions import ValidationError
from core.serializers import AuthorSerializer, BookSerializer, RegisterSerializer
from django.contrib.auth import get_user_model


USER = get_user_model()


@pytest.mark.django_db
def test_author_serializer_valid_data():
    data = {"name": "Jane Austen", "date_of_birth": "1775-12-16"}
    serializer = AuthorSerializer(data=data)
    assert serializer.is_valid()
    author = serializer.save()
    assert author.name == "Jane Austen"
    assert str(author.date_of_birth) == "1775-12-16"


@pytest.mark.django_db
def test_author_serializer_invalid_data():
    data = {"name": "", "date_of_birth": "invalid-date"}
    serializer = AuthorSerializer(data=data)
    assert not serializer.is_valid()
    assert "name" in serializer.errors
    assert "date_of_birth" in serializer.errors


@pytest.mark.django_db
def test_register_serializer_valid_data():
    data = {
        "username": "janedoe",
        "password": "securepassword123",
        "password2": "securepassword123",
        "email": "janedoe@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
    }
    serializer = RegisterSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.username == "janedoe"
    assert user.email == "janedoe@example.com"
    assert user.check_password("securepassword123")


@pytest.mark.django_db
def test_register_serializer_password_mismatch():
    data = {
        "username": "user",
        "email": "user@example.com",
        "password": "password123",
        "password2": "password456",
        "first_name": "First",
        "last_name": "Last",
    }
    serializer = RegisterSerializer(data=data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_register_serializer_unique_email():
    USER.objects.create_user(
        username="johndoe", password="password123", email="johndoe@example.com"
    )
    data = {
        "username": "janedoe",
        "password": "password123",
        "password2": "password123",
        "email": "johndoe@example.com",  # Duplicate email
        "first_name": "Jane",
        "last_name": "Doe",
    }
    serializer = RegisterSerializer(data=data)
    assert not serializer.is_valid()
    assert "email" in serializer.errors


@pytest.mark.django_db
def test_book_serializer_valid_data(author_fixture):
    data = {
        "title": "Pride and Prejudice",
        "author": author_fixture.id,
        "published_at": "1813-01-28",
        "genre": "Romance",
        "is_archived": False,
    }
    serializer = BookSerializer(data=data)
    assert serializer.is_valid()
    book = serializer.save()
    assert book.title == "Pride and Prejudice"
    assert book.author == author_fixture
    assert str(book.published_at) == "1813-01-28"


@pytest.mark.django_db
def test_book_serializer_invalid_data(author_fixture):
    data = {
        "title": "",
        "author": author_fixture.id,
        "published_at": "invalid-date",
        "genre": "",
        "is_archived": False,
    }
    serializer = BookSerializer(data=data)
    assert not serializer.is_valid()
    assert "title" in serializer.errors
    assert "published_at" in serializer.errors
    assert "genre" in serializer.errors
