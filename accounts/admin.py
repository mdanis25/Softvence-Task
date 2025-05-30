from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 

@admin.register(CustomUser) 
class CustomUserAdmin(UserAdmin): 
    list_display = ['id','email', 'username', 'password', 'is_staff', 'is_active']
    