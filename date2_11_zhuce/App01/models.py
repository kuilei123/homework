from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=128)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=20)

    class Meta:
        db_table='user'