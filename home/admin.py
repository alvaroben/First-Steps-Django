from django.contrib import admin
from home.models import Car


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    pass


admin.site.register(Car, CarAdmin)
