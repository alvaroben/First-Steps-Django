from django.urls import path

from home.views import HomeView, CarUpdate, DeleteView, CarDelete, CarCreate

urlpatterns = [
    path("", HomeView.as_view(), name="home_url"),
    path("update_car/<int:pk>", CarUpdate.as_view(), name="update_car_url"),
    path("delete_car/<int:pk>", CarDelete.as_view(), name="delete_car_url"),
    path("create_car/", CarCreate.as_view(), name="create_car_url"),
]
