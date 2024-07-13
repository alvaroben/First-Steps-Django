from django.contrib import admin

from login.models import UserType, MyUser

admin.site.register(UserType)
admin.site.register(MyUser)
