from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class restaurant(models.Model):
    Restaurant_name=models.CharField(max_length=50,default=None)
    Restaurant_photo=models.ImageField(upload_to='restaurant_images/')
    status=models.BooleanField(default=False)
    password=models.CharField(default=None,max_length=30)
    uname=models.CharField(max_length=30,default=None)
    email=models.CharField(max_length=50,default=None)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    def __str__(self):
        return self.Restaurant_name
    
class Category(models.Model):
    id=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=20,default="Special")
    
    def __str__(self):
        return self.cname
   
class Item(models.Model):
    id=models.AutoField(primary_key=True)
    rdata=models.ManyToManyField(restaurant,related_name='rest_items')
    pname=models.CharField(max_length=50,unique=True)
    pdesc=models.CharField(max_length=150,default="delicious")
    price=models.DecimalField(max_digits=6,decimal_places=2)
    pimage=models.ImageField(upload_to='menu_images/')
    category=models.CharField(max_length=150,default="delicious")
    discount=models.DecimalField(max_digits=3,decimal_places=0,default=0)
    
    def __str__(self):
        return self.pname
    

       
class Order(models.Model):
    id=models.AutoField(primary_key=True)
    created_on=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    items=models.ManyToManyField('Item',related_name="order",blank=True)
    
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'

class demo(models.Model):
    name=models.CharField(max_length=10)