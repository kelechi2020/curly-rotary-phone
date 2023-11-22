import django_filters.rest_framework
from django.shortcuts import render
from django_filters import rest_framework as django_filters
from rest_framework import viewsets, permissions

from books.filters import BookFilter
from books.models import Book
from books.serializer import BookSerializer


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    """
    Employee endpoint  provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = BookFilter