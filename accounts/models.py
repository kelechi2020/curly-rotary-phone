from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    """
    Extending the Abstract user class to add extra fields that allow a user assume
    one or more roles on the platform
    """

    is_reader = models.BooleanField(default=False, db_index=True)
    is_author = models.BooleanField(default=False, db_index=True)


class Activity(models.Model):
    """
    Generic model for tracking object level activities
    """

    FAVORITE = "F"
    ACTIVITY_TYPES = ((FAVORITE, "Favorite"),)

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        unique_together = ["user", "object_id"]
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
