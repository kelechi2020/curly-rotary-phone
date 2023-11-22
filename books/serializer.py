from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.first_name")

    class Meta:
        model = Book
        fields = [
            "book_number",
            "author",
            "title",
            "description",
            "publish_date",
        ]
        extra_kwargs = {
            "publish_date": {"format": "%Y-%m-%d"},
        }
