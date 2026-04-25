from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer 
from .permissions import IsAdminOrFaculty
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAdminUser]
        
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAdminOrFaculty]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]