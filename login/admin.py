from django.contrib import admin

from home.models import Car

class CarAdmin(admin.ModelAdmin):
    pass
# admin.site.register(UserType)
# admin.site.register(MyUser)
admin.site.register(Car, CarAdmin)