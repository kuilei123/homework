from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.db import models


class User(AbstractUser):
    # username=models.CharField(max_length=30)
    password=models.CharField(max_length=128)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=20)

    class Meta:
        db_table='user'
