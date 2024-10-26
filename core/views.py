from django.core.cache import cache
from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters
from rest_framework import generics, permissions, viewsets, response, status
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, RegisterSerializer


USER = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = USER.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class BookFilter(filters.FilterSet):
    published_date_range = filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ["author", "genre", "published_date_range"]


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.select_related("author").all()
    filterset_class = BookFilter
    filter_backends = [
        filters.DjangoFilterBackend,
    ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def list(self, request, *args, **kwargs):
        cache_key = "book_list"

        cached_data = cache.get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=600)
        return response

    def create(self, request, *args, **kwargs):

        cache.delete("book_list")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        cache.delete("book_list")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):

        cache.delete("book_list")
        return super().destroy(request, *args, **kwargs)
