from django.db import models

# Create your models here.
class user(models.Model):
    id=models.IntegerField(primary_key=True)
    uname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    
class customer(models.Model):
    id=models.IntegerField(primary_key=True)
    uname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=150)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=6)
    
    def __str__(self):
        return self.uname
    
