from __future__ import annotations

from apps.posts.models import User
from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    displayName = filters.CharFilter(
        field_name='displayName', lookup_expr='icontains',
    )

    class Meta:
        model = User
        fields = ['displayName']
