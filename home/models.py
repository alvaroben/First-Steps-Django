from django.db import models


class Car(models.Model):
    CAR_TYPE = (
        ("jeepeta", "Jeepeta"),
        ("camioneta", "Camioneta"),
        ("deportivos", "Deportivos"),
        ("sedan", "sedan"),
        ("camion", "Camion")
    )

    CONDITION = (
        ("new", "New"),
        ("used", "Used")
    )

    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    CAR_TYPE = models.CharField(max_length=50, choices=CAR_TYPE)
    condition = models.CharField(max_length=50, choices=CONDITION, default="new")
    year = models.IntegerField()
# Create your models here.
