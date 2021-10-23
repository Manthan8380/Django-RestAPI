from django.db import models

# Create your models here.

class employees(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email_Id = models.CharField(max_length=25)
    emp_Id =models.IntegerField()

class User(models.Model):
    pass