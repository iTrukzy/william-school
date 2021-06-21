from classes.models import Class
from django.db import models

# Create your models here.
class Student(models.Model):
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.IntegerField(max_length=10)
    celphone = models.IntegerField(max_length=100)  
    birth_date = models.DateField(null=True)
    description = models.CharField(max_length=300, null=True)
    class_signed = models.ManyToManyField(
        Class,
        related_name='students'
    )


    def __str__(self):
        return self.firt_name