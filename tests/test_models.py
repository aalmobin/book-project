import pytest
from core.models import Author, Book, BookLog


@pytest.mark.django_db
def test_author_creation():
    author = Author.objects.create(name="John Doe", date_of_birth="1970-01-01")
    assert author.name == "John Doe"
    assert str(author.date_of_birth) == "1970-01-01"
    assert str(author) == "John Doe"


@pytest.mark.django_db
def test_book_creation():
    author = Author.objects.create(name="John Doe", date_of_birth="1970-01-01")
    book = Book.objects.create(
        title="Test Book", author=author, published_at="2000-01-01", genre="Fiction"
    )
    assert book.title == "Test Book"
    assert book.author == author
    assert str(book) == "Test Book | John Doe"


@pytest.mark.django_db
def test_booklog_creation():
    log = BookLog.objects.create(
        book_title="Test Book", author_name="John Doe", action="create"
    )
    assert log.action == "create"
    assert log.book_title == "Test Book"
    assert str(log) == "Test Book - create"
