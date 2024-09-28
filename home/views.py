from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from home.models import Car

class ModelDeleteView(DeleteView):
    model = Car
    fields = ["brand","model","car_type","year",]
    success_url = reverse_lazy("home_url")



class HomeView(ListView):
    model = Car


class CarUpdate(UpdateView):
    model = Car
    fields = ["brand","model","car_type","year",]
    success_url = reverse_lazy("home_url")

class  createcar(CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("home_url")



