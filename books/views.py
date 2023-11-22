import logging

from django_filters import rest_framework as django_filters
from rest_framework import viewsets, permissions

from books.filters import BookFilter
from books.models import Book
from books.serializer import BookSerializer

logger = logging.getLogger(__name__)


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Books endpoint  provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions
    """

    queryset = Book.objects.all()
    lookup_field = "book_number"
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = BookFilter
