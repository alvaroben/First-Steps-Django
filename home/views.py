from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from login.models import MyUser


@login_required
def home_view(request):
    user = MyUser.objects.last()
    return render(request, "login/home.html", {"user": user})
