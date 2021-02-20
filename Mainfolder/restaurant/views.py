from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import auth
from restaurant.models import Restaurant_manager
# Create your views here.


def home(request):
    return render(request,"restaurant/rHome.html")

def r_login(request):
    if request.method=="POST":
       email=request.POST['email']
       password=request.POST['password']
       if Restaurant_manager.objects.filter(email=email,password=password).exists():
           user=Restaurant_manager.objects.get(email=email,password=password)
           if user is not None:
               return render(request,"restaurant/rHome.Html",context=user)
       else:
           return HttpResponse("not find")
    else:
        return render(request,'restaurant/r_login.html')
def r_signup(request):
    if request.method=="POST":
       restname=request.POST['restname']
       restphoto=request.POST['restphoto']
       uname=request.POST['username']
       email=request.POST['email']
       mobileno=request.POST['mobileno']
       cpassword=request.POST['password']
       password=request.POST['cpassword']
       address=request.POST['address']
       state=request.POST['state']
       city=request.POST['city']
       zipcode=request.POST['zipcode']
       if cpassword==password:
           user=Restaurant_manager( Restaurant_name=restname,name=uname,email=email,mobile=mobileno,password=cpassword,address=address,state=state,city=city,zipcode=zipcode)
           if user is not None:
               user.save()
               return render(request,"restaurant/r_login.html")
       else:
           return HttpResponse("something went wrong")
    else:
        return render(request,'restaurant/r_register.html')
    