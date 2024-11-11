import pytest
from django.contrib.auth import get_user_model
from core.models import Author, Book
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

USER = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(scope="function")
def author_fixture(db):
    author = Author.objects.create(name="John Doe", date_of_birth="1970-01-01")
    return author


@pytest.fixture(scope="function")
def book_fixture(db, author_fixture):
    book = Book.objects.create(
        title="Test Book",
        author=author_fixture,
        published_at="2000-01-01",
        genre="Fiction",
    )
    return book


@pytest.fixture
def user():
    return USER.objects.create_user(username="testuser", password="testpassword")


@pytest.fixture
def token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


@pytest.fixture
def authenticated_client(api_client, token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


@pytest.fixture(autouse=True)
def configure_dummy_cache(settings):
    settings.CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }
