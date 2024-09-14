from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from home.models import Car


class HomeView(ListView):
    model = Car


class CarUpdate(UpdateView):
    model = Car
    fields = ["brand", "car_type", "year", "condition" ]
    success_url = reverse_lazy("home_url")


class CarDelete(DeleteView):
    model = Car
    fields = ["brand", "car_type", "year", "condition" ]
    success_url = reverse_lazy("home_url")


    def get_queryset(self):
        return Car.objects.all()

