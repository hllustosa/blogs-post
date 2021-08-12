from rest_framework import serializers
from .models import Post

class PostCreationRequestSerializer(serializers.ModelSerializer):

    def create_post(self):
        return Post(**self.initial_data)

    class Meta:
        model = Post
        fields = ('title', 'content')
    
class PostCreationResponseSerializer(serializers.ModelSerializer):

    user = serializers.RelatedField(source='users', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user_id')

class PostSearchRequestSerializer(serializers.ModelSerializer):

    user = serializers.RelatedField(source='users', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user_displayName', 'published', 'updated')
