from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from login.forms import LoginForm
from login.models import MyUser


class MyLoginView(LoginView):
    template_name = 'login/login.html'
    success_url = reverse_lazy("home_url")
    form_class = LoginForm


def my_logout(request):
    logout(request)
