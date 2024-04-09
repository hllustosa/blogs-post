from __future__ import annotations

from rest_framework import permissions


class HasPostOwnership(metaclass=permissions.BasePermissionMetaclass):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return request.user.id == obj.user_id
