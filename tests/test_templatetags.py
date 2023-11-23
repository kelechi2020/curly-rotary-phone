
from django.test import TestCase
from books.templatetags.book_extras import is_favorite
from tests.factories import UserFactory, BookFactory, ActivityFactory


class IsFavoriteTemplateTagTest(TestCase):
    def test_is_favorite(self):
        user = UserFactory()
        book = BookFactory()
        ActivityFactory(user=user, content_object=book)

        self.assertTrue(
            is_favorite(book, user), "The book should be a favorite of the user"
        )

    def test_is_not_favorite(self):
        user = UserFactory()
        book = BookFactory()

        self.assertFalse(
            is_favorite(book, user), "The book should not be a favorite of the user"
        )
