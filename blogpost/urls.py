from django.urls import path
from apps.users.views import UserView, UserDetailsView, CurrentUserView, LoginView
from apps.posts.views import PostView, PostDetailsView, PostSearchView

urlpatterns = [
    path('users/me', CurrentUserView.as_view()),
    path('users/<str:id>', UserDetailsView.as_view()),
    path('users', UserView.as_view()),
    path('login', LoginView.as_view()),
    path('posts/search', PostSearchView.as_view()),
    path('posts/<str:id>', PostDetailsView.as_view()),
    path('posts', PostView.as_view()),
]
