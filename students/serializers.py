from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from students.models import Student


class StudentSerializer(ModelSerializer):

    def validate(self, attrs):
        if '{' in attrs['firt_name']:
            raise serializers.ValidationError('Nombe no valido')
        return attrs
    class Meta:
        model = Student
        fields = ('firt_name', 'last_name', 'email', 'age', 'celphone', 'birth_date', 'description', 'class_signed')

