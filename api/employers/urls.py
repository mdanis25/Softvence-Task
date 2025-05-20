from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployerViewSet 

router = DefaultRouter()
router.register('employers', EmployerViewSet, basename='employer')

urlpatterns = [ 
    path('', include(router.urls)),
]
