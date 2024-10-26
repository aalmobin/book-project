from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Book, BookLog


@receiver(post_save, sender=Book)
def create_book_log(sender, instance, created, **kwargs):
    if created:
        BookLog.objects.create(
            book_title=instance.title,
            author_name=instance.author.name,
            action="create",
        )


@receiver(post_delete, sender=Book)
def delete_book_log(sender, instance, **kwargs):
    BookLog.objects.create(
        book_title=instance.title, author_name=instance.author.name, action="delete"
    )
