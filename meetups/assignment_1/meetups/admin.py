from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# these are for classes? or something


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile)