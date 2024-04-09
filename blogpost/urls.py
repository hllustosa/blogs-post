from __future__ import annotations

from apps.posts.views import PostDetailsView
from apps.posts.views import PostSearchView
from apps.posts.views import PostView
from apps.users.views import CurrentUserView
from apps.users.views import LoginView
from apps.users.views import UserDetailsView
from apps.users.views import UserView
from django.urls import path

urlpatterns = [
    path('users/me', CurrentUserView.as_view()),
    path('users/<str:id>', UserDetailsView.as_view()),
    path('users', UserView.as_view()),
    path('login', LoginView.as_view()),
    path('posts/search', PostSearchView.as_view()),
    path('posts/<str:id>', PostDetailsView.as_view()),
    path('posts', PostView.as_view()),
]
