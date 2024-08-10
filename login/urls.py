from django.urls import path
from login.views import MyLoginView, my_logout

urlpatterns = [
    path("", MyLoginView.as_view(), name="login_url"),
    path("logout", my_logout, name="logout_url"),
]
