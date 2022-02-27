from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    username = models.EmailField(primary_key = True)
    password = models.CharField(max_length = 200)
    is_admin = models.BooleanField(default = False)
    name = models.CharField(max_length=50)
    email = models.EmailField()


# Create your models here.
