from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    student_id = models.CharField(max_length=20, unique=True) 
    full_name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True) 
    course = models.CharField(max_length=100) 
    year_level = models.IntegerField() 

    def __str__(self):
        return self.full_name 