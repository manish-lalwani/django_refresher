from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser1  # Replace with your actual model name

admin.site.register(CustomUser1, UserAdmin)
# Register your models here.
