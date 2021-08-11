from django.db import models
from users.models import User

class Post(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    title = models.CharField(blank=False, null=False, max_length=100)
    content = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    published = models.DateTimeField(null=False)
    updated = models.DateTimeField()
