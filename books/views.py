import logging

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, CreateView
from django_filters import rest_framework as django_filters
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Activity
from books.filters import BookFilter
from books.forms import BookForm
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


class BookListView(generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.prefetch_related("favorites")


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    template_name = "books/book_update.html"
    fields = [
        "title",
        "author",
        "description",
    ]

    def get_success_url(self):
        return reverse_lazy("books")

    def test_func(self):
        return self.request.user.is_staff


class FavoritesView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = "books/my_favorites.html"

    def get_queryset(self):
        book_content_type = ContentType.objects.get_for_model(Book)

        favorite_book_ids = Activity.objects.filter(
            user=self.request.user,
            activity_type=Activity.FAVORITE,
            content_type=book_content_type,
        ).values_list("object_id", flat=True)

        favorite_books = Book.objects.filter(id__in=favorite_book_ids)

        return favorite_books


class ToggleFavoriteView(LoginRequiredMixin, APIView):
    """
    View to toggle the favorite status of a book for logged in user.
    """

    def post(self, request, book_id, format=None):
        book = get_object_or_404(Book, pk=book_id)

        favorite = book.favorites.filter(
            book__book_number=book.book_number,
            user=request.user,
            object_id=book.id,
            activity_type=Activity.FAVORITE,
        )

        if favorite.exists():
            print("deleted")
            favorite.delete()
            is_favorite = False
        else:
            book.favorites.create(
                user=request.user, object_id=book.id, activity_type=Activity.FAVORITE
            )
            print("created")
            is_favorite = True

        return Response({"is_favorite": is_favorite}, status=status.HTTP_200_OK)


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_create.html"
    success_url = reverse_lazy("books")

    def test_func(self):
        return self.request.user.is_staff
