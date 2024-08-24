from django.db import models

# Create your models here.

class Car (models.Model):
    car_TYPE = (("jepeta", "Jepeta"),
                ("camioneta", "Camioneta"),
                ("deportivo", "Deportivo"),
                ("seldan", "Selda"))



    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50, choices=car_TYPE)
    year = models.IntegerField()