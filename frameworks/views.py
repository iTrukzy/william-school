

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from students.serializers import CreateStudentSerializer, StudentSerializer
from students.models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


# @api_view(['GET', 'POST'])
# def hola(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serialized = StudentSerializer(students, many=True)
#         return Response(data=serialized.data)


#     if request.method == 'POST':
#         serialized = StudentSerializer(data=request.data)
#         if not serialized.is_valid():
#             return Response(
#                 status=status.HTTP_400_BAD_REQUEST,
#                 data=serialized.errors
#             )
#         serialized.save()

#         return Response(status=status.HTTP_201_CREATED, data=serialized.data)


# @api_view(['PUT', 'PATCH', 'GET', 'DELETE'])
# def student(request, student_id):
#     student = Student.objects.get(id=student_id)
#     if request.method == 'GET':
#         serialized = StudentSerializer(student, many=False)
#         return Response(data=serialized.data)


#     if request.method == 'PUT':
#         serialized = StudentSerializer(instance=student, data=request.data)

#         if not serialized.is_valid():
#             return Response(
#                 status=status.HTTP_400_BAD_REQUEST,
#                 data=serialized.errors
#             )

#         serialized.save()
#         return Response(status=status.HTTP_200_OK)

#     if request.method == 'PATCH':
#         serialized = StudentSerializer(instance=student, data=request.data, partial=True)

#         if not serialized.is_valid():
#             return Response(
#                 status=status.HTTP_400_BAD_REQUEST,
#                 data=serialized.errors
#             )

#         serialized.save()
#         return Response(status=status.HTTP_200_OK)


#     if request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_200_OK)
    

# class StudentGenericView(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class DetailStudentGenericView(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# # class StudentViewSet(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = (IsAuthenticated, )

#     def get_permissions(self):
#         user = User.objects.all().values()
#         permissions = []
#         if self.request.method == 'GET':
#             permissions = (AllowAny, )
#         elif self.request.method == 'DELETE' and user:
#             permissions = (IsAuthenticated, )
#         else:
#             permissions = (IsAuthenticated, )

#         return [permissions() for permissions in permissions]