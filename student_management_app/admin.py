from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
# Register your models here.


class UserModel(UserAdmin):
    pass


admin.site.register(models.CustomerUser, UserModel)