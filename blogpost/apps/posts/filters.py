from __future__ import annotations

from apps.posts.models import Post
from django_filters import rest_framework as filters


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = filters.CharFilter(field_name='content', lookup_expr='icontains')
    user_id = filters.CharFilter(field_name='user_id', lookup_expr='exact')

    class Meta:
        model = Post
        fields = ['title', 'content', 'user_id']
