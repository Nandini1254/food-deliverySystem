from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import auth
from OrderingOnline.models import customer
# Create your views here.


def index(request):
    return render(request,"OrderingOnline/index.html")

def about(request):
    return render(request,"OrderingOnline/about.html")

def login_category(request):
    return render(request,"OrderingOnline/login_category.html")

def register_category(request):
    return render(request,"OrderingOnline/register_category.html")

def login(request):
    if request.method=="POST":
       email=request.POST['email']
       password=request.POST['password']
       if customer.objects.filter(email=email,password=password).exists():
           user=customer.objects.get(email=email,password=password)
           if user is not None:
               return HttpResponse("yessss {}".format(user.uname))
       else:
           return HttpResponse("not find")
    else:
        return render(request,'OrderingOnline/login.html')
def signup(request):
    if request.method=="POST":
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
           user=customer(uname=uname,email=email,mobile=mobileno,password=cpassword,address=address,state=state,city=city,zipcode=zipcode)
           if user is not None:
               user.save()
               return HttpResponse("yessss")
       else:
           return HttpResponse("not added")
    else:
        return render(request,'OrderingOnline/register.html')
    