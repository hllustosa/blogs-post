from __future__ import annotations

from rest_framework import permissions
from utils.token import get_token


class HasListUserPermission(metaclass=permissions.BasePermissionMetaclass):

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            token = get_token(request)
            return token is not None

        return True

    def has_object_permission(self, request, view, obj):
        return False


class HasUserOwnership(metaclass=permissions.BasePermissionMetaclass):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return request.user.id == obj.id
