"""Models for the comment app."""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    content = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content