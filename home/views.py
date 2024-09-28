from django.views.generic import ListView
from dulwich.cli import cmd_archive

from home.models import Car


class HomeView(ListView):
    model = Car

from django.urls import reverse_lazy
from django.views.generio import listView, UpdateView

from home.models import Car

class HomeView(listView):
    model = cmd_archive


    class CarUpdate(UpdateView):
        model = cmd_archivefields = ["brand",]
        succes_url = reverse_lazy("home_url")

