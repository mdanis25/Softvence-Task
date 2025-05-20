from rest_framework import viewsets 
from employers.models import Employer
from .serializers import EmployerSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class EmployerViewSet(viewsets.ModelViewSet):   
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated, IsOwner] # only see his/her details

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 