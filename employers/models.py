from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import get_user_model 

class Employer(models.Model): 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="employers")  #CustomUser = User = get_user_model
    company_name = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
