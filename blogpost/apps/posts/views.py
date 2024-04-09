from __future__ import annotations

from apps.posts.filters import PostFilter
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from rest_framework import generics
from utils.permission import BlogPostHasObjPermission
from utils.permission import BlogPostPermission


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [BlogPostPermission]
    filterset_class = PostFilter


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [BlogPostHasObjPermission]
