from django.db import models

# Create your models here.
class Car (models.Model):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    year = models.IntegerFieldField()