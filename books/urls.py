from django.urls import path, include
from books import views


urlpatterns = [
    path("", views.BookListView.as_view(), name="books"),
    path("books/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    path("books/create", views.BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/update", views.BookUpdateView.as_view(), name="book-update"),
    path(
        "user/<int:pk>/favorite",
        views.FavoritesView.as_view(),
        name="user-favorites",
    ),
    path(
        "books/<int:book_id>/favorite",
        views.ToggleFavoriteView.as_view(),
        name="toggle-favorite",
    ),
]
