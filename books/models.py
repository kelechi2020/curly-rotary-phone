from datetime import date

from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from accounts.models import Activity

from django.contrib.auth import get_user_model
User = get_user_model()


class AuditTrail(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(AuditTrail):
    book_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="book")
    description = models.TextField(blank=True)
    publish_date = models.DateField(default=date.min, blank=True, null=True)
    count = models.IntegerField(default=0, blank=True, null=True)
    favorites = GenericRelation(Activity, related_query_name="book")

    def clean(self):
        errors = {}
        if self.publish_date > date.today():
            errors["publish_date"] = "publish_date can only be set in the past."

        if errors:
            raise ValidationError(errors)

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse("book_detail", args=[str(self.id)])

    class Meta:
        ordering = ("title",)
        verbose_name = "Book"
        verbose_name_plural = "Books 📚"

    def __str__(self):
        return self.title
