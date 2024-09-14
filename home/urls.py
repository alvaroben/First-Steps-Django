from django.urls import path

from home.views import HomeView, CarUpdate, DeleteView

urlpatterns = [
    path("", HomeView.as_view(), name="home_url"),
    path("update_car/<int:pk>", CarUpdate.as_view(), name="update_car_url"),
    path("update_car/<int:pk>", DeleteView.as_view(), name="update_car_url") 
    ]
