from django.urls import path
from .views import *
urlpatterns = [
    path("register",RegisterUserView.as_view(), name="register"),
    path("login",LoginView.as_view(), name="login"),
    path("logout",LogoutView.as_view(), name="logout"),
    path('contactus/', ContactMessageCreateView.as_view(), name='contact-create'),
]
