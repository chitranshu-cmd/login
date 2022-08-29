import email
from django.db import models
from django.contrib.auth.models import User,auth

class Student(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  age = models.IntegerField()



def __str__(self):
     return self.name



# Create your models here.
