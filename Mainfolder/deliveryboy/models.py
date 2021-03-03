from django.db import models
#from django.db import models

# Create your models here.
class deliveryboy_manager(models.Model):
    id=models.IntegerField(primary_key=True)
    deliveryboy_name=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    uname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=150)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=6)
    
    def __str__(self):
        return self.deliveryboy_name
   
# Create your models here.
