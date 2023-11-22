from django.core.exceptions import ValidationError
from django.test import TestCase
from tests.factories import BookFactory
from books.models import Book
from datetime import date, timedelta


class BookModelTest(TestCase):
    def test_book_creation(self):
        book = BookFactory()
        self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.__str__(), book.title)

    def test_book_publish_date_validation(self):
        future_date = date.today() + timedelta(days=1)
        book = BookFactory.build(publish_date=future_date)
        with self.assertRaises(ValidationError) as error:
            book.clean()  # clean method should raise ValidationError
        self.assertEqual(
            error.exception.messages[0], "publish_date can only be set in the past."
        )
