from django.urls import path
from users.views import UserView, UserDetailsView, CurrentUserView, LoginView

urlpatterns = [
    path('users/me', CurrentUserView.as_view()),
    path('users/<str:id>', UserDetailsView.as_view()),
    path('users', UserView.as_view()),
    path('login', LoginView.as_view()),
]
