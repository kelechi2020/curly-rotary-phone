# books/tests/test_filters.py
from django.test import TestCase

from books.filters import BookFilter
from django.contrib.auth import get_user_model

from tests.factories import BookFactory

User = get_user_model()


class BookFilterTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 50 books with varying data
        cls.books = [BookFactory() for _ in range(50)]

    def test_filter_by_title(self):
        # Test filtering by title
        test_title = self.books[0].title
        filter_data = {"title": test_title}
        book_filter = BookFilter(data=filter_data)
        self.assertIn(self.books[0], book_filter.qs)

    def test_filter_by_author(self):
        # Test filtering by author
        test_author = self.books[0].author
        filter_data = {"author_name": test_author.first_name}
        book_filter = BookFilter(data=filter_data)
        self.assertTrue(any(book.author == test_author for book in book_filter.qs))
