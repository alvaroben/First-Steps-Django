from django.urls import path
from login.views import MyLoginView

urlpatterns = [
    path("", MyLoginView.as_view(), name="login_url"),
]
