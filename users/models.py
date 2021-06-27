from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
class UserNew(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    pagina_web = models.CharField()

class UserCustom(AbstractUser):
    pass