from __future__ import annotations

from apps.users.models import User
from django.db import models


class Post(models.Model):
    id = models.CharField(primary_key=True, max_length=35)
    title = models.CharField(blank=False, null=False, max_length=100)
    content = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    published = models.DateTimeField(null=False)
    updated = models.DateTimeField(null=True)
