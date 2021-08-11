from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    displayName = models.CharField(blank=False, null=False, max_length=100)
    email = models.CharField(blank=False, null=False, max_length=64)
    password = models.CharField(blank=False, null=False, max_length=25)
    image = models.CharField(blank=False, null=False, max_length=200)