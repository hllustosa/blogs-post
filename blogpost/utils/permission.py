from __future__ import annotations

from rest_framework import permissions
from utils.token import get_token


class IsAuthenticated(metaclass=permissions.BasePermissionMetaclass):

    def check_permisions(self, request):
        token = get_token(request)
        return token is not None

    def has_permission(self, request, view):
        return self.check_permisions(request)

    def has_object_permission(self, request, view, obj):
        return self.check_permisions(request)
