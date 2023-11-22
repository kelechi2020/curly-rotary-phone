from datetime import date

from books.views import BookViewSet
from tests.factories import BookFactory, UserFactory


from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate


class BookViewsTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = UserFactory.create()
        BookFactory.create_batch(10, title="Django for Beginners")
        BookFactory.create_batch(10, title="Advanced Django")
        BookFactory.create_batch(10, author__first_name="John")
        BookFactory.create_batch(10, author__first_name="Jane")
        BookFactory.create_batch(10, publish_date=date(2020, 1, 1))

    def test_book_filters(self):
        # Test title filter
        request = self.factory.get(reverse("book-list") + "?title__icontains=Django")
        view = BookViewSet.as_view({"get": "list"})
        force_authenticate(request, user=self.user)
        response = view(request)
        assert response.status_code == 200
        assert response.data["count"] == 20

        # Test author name filter
        request = self.factory.get(reverse("book-list") + "?author_name=John")
        view = BookViewSet.as_view({"get": "list"})
        force_authenticate(request, user=self.user)
        response = view(request)
        assert response.status_code == 200
        assert response.data["count"] == 10

        # Test publish date filter
        request = self.factory.get(reverse("book-list") + "?publish_date=2020-01-01")
        view = BookViewSet.as_view({"get": "list"})
        force_authenticate(request, user=self.user)
        response = view(request)
        assert response.status_code == 200
        assert response.data["count"] == 10
