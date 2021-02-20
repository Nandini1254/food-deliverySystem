from django.db import models

# Create your models here.
# Create your models here.
class Student(models.Model):
    user_name = models.CharField(max_length=100)
    dob = models.DateTimeField('date published')