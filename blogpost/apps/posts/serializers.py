from __future__ import annotations

from django.utils import timezone
from rest_framework import serializers
from utils.id import create_id
from utils.token import get_user_id

from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user_id', 'published', 'updated']
        read_only_fields = ['id', 'user_id', 'published', 'updated']

    def create(self, validated_data):
        current_time = timezone.localtime()
        validated_data['id'] = create_id('post')
        validated_data['user_id'] = get_user_id(self.context['request'])
        validated_data['published'] = current_time
        validated_data['updated'] = current_time
        return super().create(validated_data)

    def update(self, validated_data):
        validated_data['updated'] = timezone.localtime()
        return super().update(validated_data)

    def partial_update(self, validated_data):
        validated_data['updated'] = timezone.localtime()
        return super().partial_update(validated_data)
