from rest_framework.viewsets import ModelViewSet
from students.models import Student
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from students.serializers import StudentSerializer
from students.models import Student
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, )

    def get_permissions(self):
        user = User.objects.all().values()
        permissions = []
        if self.request.method == 'GET':
            permissions = (AllowAny, )
        elif self.request.method == 'DELETE' and user:
            permissions = (IsAuthenticated, )
        else:
            permissions = (IsAuthenticated, )

        return [permissions() for permissions in permissions]



    