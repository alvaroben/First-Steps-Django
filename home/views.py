from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

class ModelDeleteView(DeleteView):
    model = chr
    fields = ["brand","model","car_type","year",]
    success_url = reverse_lazy("home_url")


from home.models import Car


class HomeView(ListView):
    model = Car


class CarUpdate(UpdateView):
    model = Car
    fields = ["brand","model","car_type","year",]
    success_url = reverse_lazy("home_url")

