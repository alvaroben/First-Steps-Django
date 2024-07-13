from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.Model):
    name = models.CharField(verbose_name="nombre", max_length=10)

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    user_type = models.ForeignKey(UserType, null=True, blank=True, on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name="edad", default=0)
    gender = models.CharField(verbose_name="genero", choices=(("male", "Male"), ("female", "Female")), max_length=10,
                              default="male")

    # crear una funcion que devuelva una presentacion. 'Hola, soy alvaro bencosme, tengo 25 y soy hombre
    # @staticmethod
    def user_presentation(self):
        message = "Hola, soy %s, tengo %s y soy %s" % (self.first_name, self.age, self.gender)
        return message
