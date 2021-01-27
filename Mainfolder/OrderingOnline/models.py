from django.db import models

# Create your models here.
class user(models.Model):
    id=models.IntegerField(primary_key=True)
    uname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)