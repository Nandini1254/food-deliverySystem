from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurant_manager(models.Model):
    id=models.IntegerField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Restaurant_name=models.CharField(max_length=50,default="null")
    Restaurant_photo=models.ImageField(upload_to='restaurant_images/')
    status=models.BooleanField(default=False)
    uname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=150)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    def __str__(self):
        return self.Restaurant_name
   
class Item(models.Model):
    pid=models.IntegerField(primary_key=True)
    rname=models.CharField(max_length=50, default="null")
    pname=models.CharField(max_length=50)
    pdesc=models.CharField(max_length=150,default="delicious")
    price=models.DecimalField(max_digits=6,decimal_places=2)
    pimage=models.ImageField(upload_to='menu_images/')
    category=models.ManyToManyField('Category',related_name='item')
    
    def __str__(self):
        return self.pname
    
class Category(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=20)
    
    def __str__(self):
        return self.cname
    
class Order(models.Model):
    created_on=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    items=models.ManyToManyField('Item',related_name="order",blank=True)
    
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'