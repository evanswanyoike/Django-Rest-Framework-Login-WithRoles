from django.contrib import admin

from .models import AdminProfile, CustomUser

# Register your models here.

admin.site.register(AdminProfile)
admin.site.register(CustomUser)
