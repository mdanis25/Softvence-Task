 
from django.contrib import admin
from django.urls import path  
from . import views 

urlpatterns = [
    path('signup/', views.UserRegistrationAPIView.as_view(), name = 'signup'), 
    path('login/', views.UserLoginAPIView.as_view(), name = 'login'), 
    path('profile/', views.UserProfileAPIView.as_view(), name = 'profile'), 
]
