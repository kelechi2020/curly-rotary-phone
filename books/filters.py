import django_filters

from books.models import Book


class BookFilter(django_filters.filterset):
    author_name = django_filters.CharFilter(field_name="author__first_name", lookup_expr="icontains")
    publish_date = django_filters.IsoDateTimeFilter()

    class Meta:
        model = Book
        fields = {
            "title": ["icontains"],
            "description": ["icontains"],
            "publish_date": ["icontains"],
        }