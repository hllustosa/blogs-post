from django.conf.urls import url 
from users.views import UserView, LoginView

urlpatterns = [
    url(r'^users$', UserView.as_view()),
    url(r'^login$', LoginView.as_view()),
]
