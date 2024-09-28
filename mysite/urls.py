from django.urls import path

from home.Views import HomeViews, CarUpdate

urlpatterns = [
    path("", HomeView.as_View(), name="home_url"),
    path("update_car/<int:pk>", CarUpdate.as_View(), name="update_car_url"),
    ]



