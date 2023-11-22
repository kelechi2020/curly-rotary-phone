import factory
from django.contrib.auth import get_user_model
from django.utils import timezone
from books.models import Book, Activity
from random import randint
from datetime import timedelta

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    is_reader = True
    is_author = False


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    book_number = factory.Sequence(lambda n: f"BN{n:05d}")
    title = factory.Faker("sentence", nb_words=4)
    author = factory.SubFactory(UserFactory)
    description = factory.Faker("text")
    publish_date = factory.LazyFunction(
        lambda: timezone.now() - timedelta(days=randint(1, 1000))
    )
    count = factory.Sequence(lambda n: n)


class ActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Activity

    user = factory.SubFactory(UserFactory)
    activity_type = Activity.FAVORITE
    content_object = factory.SubFactory(BookFactory)
