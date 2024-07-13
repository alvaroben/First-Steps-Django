from django.urls import path
from login.views import MyLoginView, home_view

urlpatterns = [
    path("", MyLoginView.as_view(), name="login_url"),
    path("home/", home_view, name="home_url")
]
