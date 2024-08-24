from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from home.models import Car


class HomeView(ListView):
    model = Car
