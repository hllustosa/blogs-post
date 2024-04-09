from __future__ import annotations

from apps.users.models import User
from rest_framework import authentication
from utils.token import get_token

AUTH_HEADER_NAME = 'HTTP_AUTHORIZATION'
AUTH_HEADER_TYPE = 'Bearer'
IDENTIFIER_CLAIM = 'id'


class BlogPostAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        return self.get_user(request)

    def get_user(self, request):
        token = get_token(request)

        if token is None:
            return None

        try:
            user = User.objects.get(pk=token[IDENTIFIER_CLAIM])
            return user, None
        except User.DoesNotExist:
            return None
