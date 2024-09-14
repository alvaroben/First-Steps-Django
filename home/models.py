from random import choices

from django.db import models


class Car(models.Model):
    CAR_TYPES = (
        ("jeepeta", "Jeepeta"),
        ("camioneta", "Camioneta"),
        ("deportivo", "Deportivo"),
        ("sedan", "Sedán")
    )

    CONDITION = (
        ("new", "New"),
        ("used", "Used")
    )

    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50, choices=CAR_TYPES)
    condition = models.CharField(max_length=50, choices=CONDITION, default="new")
    year = models.IntegerField()

    @property
    def actions(self):
        return f"""
        <a href="/update_car/{self.id}" style="color: blue;" class="bi bi-pencil"></a>
        <a href="/delete_car/{self.id}" style="color: red" class="bi bi-trash"></a>
        """

    def get_car_name(self):
        return f"{self.brand} {self.model} {self.condition} {self.year}"
