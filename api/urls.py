 
from django.contrib import admin
from django.urls import path , include
 

urlpatterns = [ 
    path('auth/', include('api.accounts.urls')), 
    path('', include('api.employers.urls')), 
    
]
