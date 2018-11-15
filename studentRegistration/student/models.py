from django.db import models
import datetime

# Create your models here.

class  student(models.Model):
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=20)
    fname = models.CharField(max_length=40)
    roll = models.CharField(max_length=20)
    dob = models.DateField(default=datetime.datetime.today)
    email = models.EmailField(max_length = 40)
    phone = models.CharField(max_length=20)
    branch = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)
    year = models.CharField(max_length = 10)
