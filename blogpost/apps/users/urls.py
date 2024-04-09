from __future__ import annotations

from apps.users.views import CurrentUserView
from apps.users.views import LoginView
from apps.users.views import UserDetailsView
from apps.users.views import UserView
from django.urls import path

urlpatterns = [
    path('users/me', CurrentUserView.as_view(), name='current-user'),
    path('users/<str:id>', UserDetailsView.as_view(), name='detail-user'),
    path('users', UserView.as_view(), name='create-user'),
    path('login', LoginView.as_view(), name='login'),
]
