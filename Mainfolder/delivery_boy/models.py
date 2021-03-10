from django.db import models

# Create your models here.
class deliveryboy(models.Model):
    id=models.IntegerField(primary_key=True)
    deliveryboy_name=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=150)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)