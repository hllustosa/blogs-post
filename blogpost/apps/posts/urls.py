from __future__ import annotations

from apps.posts.views import PostListCreateAPIView
from apps.posts.views import PostRetrieveUpdateDestroyAPIView
from django.urls import path

urlpatterns = [
    path(
        'posts/<str:pk>', PostRetrieveUpdateDestroyAPIView.as_view(),
        name='retrieve-update-destroy',
    ),
    path('posts', PostListCreateAPIView.as_view(), name='list-create'),
]
