from django.contrib import admin

# Register your models here.

from Users.models import CustomUser
admin.site.register(CustomUser)

from Users.models import users
admin.site.register(users)