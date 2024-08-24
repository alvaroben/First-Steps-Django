from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView
from login.models import MyUser

from home.models import Car

#@login_required
#def home_view(request):
#    user = MyUser.objects.last()
#    return render(request, "login/home.html", {"user": user})


class HomeView(ListView):
    model = Car
