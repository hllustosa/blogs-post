from __future__ import annotations

from rest_framework import permissions
from utils.token import get_token


class BlogPostPermission(metaclass=permissions.BasePermissionMetaclass):

    def check_permisions(self, request):
        token = get_token(request)
        return token is not None

    def has_permission(self, request, view):
        return self.check_permisions(request)

    def has_object_permission(self, request, view, obj):
        return self.check_permisions(request)


class BlogPostHasObjPermission(metaclass=permissions.BasePermissionMetaclass):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return request.user.id == obj.user_id


class BlogPostCreateListUserPermission(metaclass=permissions.BasePermissionMetaclass):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'HEAD', 'OPTIONS']:
            return True

        return request.user.id == obj.user_id
