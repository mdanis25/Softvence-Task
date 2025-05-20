from django.contrib import admin
from . models import Employer  


@admin.register(Employer) 
class EmployerAdmin(admin.ModelAdmin): 
    list_display = ['id', 'company_name', 'contact_person_name', 'email','phone_number', 'address', 'created_at']