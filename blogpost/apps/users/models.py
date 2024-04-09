from __future__ import annotations

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=35)
    displayName = models.CharField(blank=False, null=False, max_length=100)
    email = models.CharField(blank=False, null=False, max_length=64)
    password = models.CharField(blank=False, null=False, max_length=200)
    image = models.CharField(blank=False, null=False, max_length=200)

    def has_valid_display_name(self):

        if not self.displayName:
            self.notification = '"displayName" is required'
            return False

        if self.displayName is None or len(self.displayName) < 8:
            self.notification = '"displayName" length must be at least 8 characters long'
            return False

        return True

    def has_valid_email(self):

        if self.email is None or not self.email:
            self.notification = '"email" is required'
            return False

        try:
            validate_email(self.email)
        except ValidationError:
            self.notification = '"email" must be a valid email'
            return False

        return True

    def has_valid_password(self):

        if self.password is None or not self.password:
            self.notification = '"password" is required'
            return False

        if len(self.password) < 6:
            self.notification = '"password" length must be at least 8 characters long'
            return False

        return True

    def has_existing_email(self):

        if User.objects.filter(email=self.email).exists():
            self.notification = 'Usuário já existe'
            return True

        return False
