from classes.serializers import ClassSerializer
from classes.models import Class
from django.shortcuts import render
from students.models import Student
from django.views import View


# Create your views here.
# Create your views here.

class Classes(View):
    def __init__(self, content = {}):
        self.content = content

    def get(self, request):
        try:
            result = Class.objects.all()
            self.content = {
                "classes": result
            }
        except OSError as err:
            self.content =  {}

        return render(request, 'classes/index.html', self.content)


    
# class oneClass(View):
#     def __init__(self, content = {}):
#         self.content = content

#     def get(self, request, id):
#         try:
#             students = Student.objects.filter(class_signed=id)
#             if students:
#                 self.content = {
#                     "students": students
#                 }
#             else:
#                 self.content = {}
#         except OSError as err:
#             self.content =  {}

#         return render(request, 'classes/details.html', self.content)

from rest_framework.viewsets import ModelViewSet
from students.models import Student
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from students.serializers import StudentSerializer
from students.models import Student
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
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
