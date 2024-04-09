from __future__ import annotations

from apps.posts.views import PostDetailsView
from apps.posts.views import PostSearchView
from apps.posts.views import PostView
from django.urls import path

urlpatterns = [
    path('posts/search', PostSearchView.as_view(), name='search-posts'),
    path('posts/<str:id>', PostDetailsView.as_view(), name='detail-post'),
    path('posts', PostView.as_view(), name='create-posts'),
]
