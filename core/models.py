from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_at = models.DateField()
    genre = models.CharField(max_length=255)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.author.name}"


class BookLog(models.Model):
    ACTION_CHOICES = [
        ("create", "Created"),
        ("delete", "Deleted"),
    ]

    book_title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book_title} - {self.action}"
