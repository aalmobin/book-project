import pytest
from core.models import Book, BookLog


@pytest.mark.django_db
def test_book_log_created_on_creation(author_fixture):
    book = Book.objects.create(
        title="New Book",
        author=author_fixture,
        published_at="2000-01-01",
        genre="History",
    )
    log = BookLog.objects.filter(book_title="New Book", action="create").first()
    assert log is not None


@pytest.mark.django_db
def test_book_log_creation_on_deletion(author_fixture):
    book = Book.objects.create(
        title="New Book",
        author=author_fixture,
        published_at="2000-01-01",
        genre="History",
    )
    book.delete()
    log = BookLog.objects.filter(book_title="New Book", action="delete").first()
    assert log is not None
