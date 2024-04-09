from __future__ import annotations

from apps.users.serializers import UserSearchRequestSerializer
from rest_framework import serializers

from .models import Post


class PostCreationRequestSerializer(serializers.ModelSerializer):

    def create_post(self):
        return Post(**self.initial_data)

    class Meta:
        model = Post
        fields = ('title', 'content')


class PostCreationResponseSerializer(serializers.ModelSerializer):

    userId = serializers.CharField(source='user_id')

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'userId')


class PostUpdateResponseSerializer(serializers.ModelSerializer):

    userId = serializers.CharField(source='user_id')

    class Meta:
        model = Post
        fields = ('title', 'content', 'userId')


class PostSearchRequestSerializer(serializers.ModelSerializer):

    user = UserSearchRequestSerializer()

    class Meta:
        model = Post
        fields = ('id', 'published', 'updated', 'title', 'content', 'user')
