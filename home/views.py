from django.views.generic import ListView

from home.models import Car


class HomeView(ListView):
    model = Car


