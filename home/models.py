from django.db import models


class Car(models.Model):
    CAR_TYPES = (
        ("jeepeta", "Jeepeta"),
        ("camioneta", "Camioneta"),
        ("deportivo", "Deportivo"),
        ("sedan", "Sedán")
    )

    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50, choices=CAR_TYPES)
    year = models.IntegerField()

    @property
    def actions(self):
        return """
        <i style="color: blue;" class="bi bi-pencil"></i>
        <i style="color: red" class="bi bi-trash"></i>
        """
