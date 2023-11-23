from django import template
from accounts.models import Activity

register = template.Library()


@register.filter(name="is_favorite")
def is_favorite(book, user):
    return book.favorites.filter(
        book__book_number=book.book_number,
        user=user,
        object_id=book.id,
        activity_type=Activity.FAVORITE,
    ).exists()
