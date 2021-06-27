from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from classes.models import Class


class ClassSerializer(ModelSerializer):

    def validate(self, attrs):
        if '{' in attrs['class_name']:
            raise serializers.ValidationError('Nombe no valido')
        return attrs
    class Meta:
        model = Class
        fields = ('class_name', )

