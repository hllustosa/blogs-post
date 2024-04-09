from __future__ import annotations

from django.urls import include
from django.urls import path

urlpatterns = [
    path('api/v1/', include(('apps.users.urls', 'users')), name='users'),
    path('api/v1/', include(('apps.posts.urls', 'posts')), name='posts'),
]
