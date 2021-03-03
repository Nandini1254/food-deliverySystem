from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import auth
from .models import deliveryboy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
# Create your views here.


def home(request):
    return render(request,"delivery_boy/d_Home.html")

def d_login(request):
    if request.method=="POST":
       username=request.POST['uname']
       password=request.POST['password']
       user1 = auth.authenticate(username=username,password=password)
       print(user1)
       if user1 is not None:
           print("yes")
           if deliveryboy.objects.filter(deliveryboy_name=username,password=password).exists():
                user=deliveryboy.objects.get(deliveryboy_name=username,password=password)
                request.session["d_name"]=user.deliveryboy_name
                request.session['d_city']=user.city
                request.session['d_state']=user.state
                request.session['d_address']=user.address
                request.session['d_status']=user.status
                request.session['d_mobile']=user.mobile
                request.session['d_email']=user.email
                return HttpResponseRedirect("/delivery_boy/home")
       else:
           return HttpResponse("not find")
    return render(request,'delivery_boy/d_login.html')
    
    
def d_signup(request):
    if request.method=="POST":
       deliveryboy_name=request.POST['username']      
       email=request.POST['email']
       mobileno=request.POST['mobileno']
       cpassword=request.POST['password']
       password=request.POST['cpassword']
       address=request.POST['address']
       state=request.POST['state']
       city=request.POST['city']
       if cpassword==password:
           user1=User.objects.create_user(username=deliveryboy_name,email=email,password=password)
           if user1 is not None:
               user=deliveryboy( deliveryboy_name=deliveryboy_name,status=False,email=email,mobile=mobileno,password=cpassword,address=address,state=state,city=city)
               print(user)
               if user is not None:
                   user.save()
                   user1.save()
                   return render(request,"delivery_boy/d_login.html")
    return render(request,'delivery_boy/d_register.html')
    
# Create your views here.
def update(request):
    if request.method=="POST":
       mobileno=request.POST['mobileno']
       address=request.POST['address']
       state=request.POST['state']
       city=request.POST['city']
       email=request.session['d_email']
       if deliveryboy.objects.filter(email=email).exists():
           user=deliveryboy_manager.objects.get(email=email)
           if user is not None:          
               user.mobileno=mobileno
               user.state=state
               user.city=city
               user.address=address
               request.session["d_name"]=user.deliveryboy_name
               request.session['d_city']=user.city
               request.session['d_state']=user.state
               request.session['d_address']=user.address
               request.session['d_mobile']=user.mobile 
               user.save()
               messages="successfully inserted"
               return render(request,'/delivery_boy/profile.html',{"mess":messages})
           else:
               return HttpResponse("something went wrong")
    else:
        return render(request,'delivery_boy/profile.html')
       
def profile_show(request):
    return render(request,"delivery_boy/d_profile.html")


def logout_deliveryboy(request):
    if request.session['d_email']:
        request.session.flush()
    return HttpResponseRedirect("delivery_boy/d_login")


def change_password(request):
    context={}
    if request.method=='POST':
        current=request.POST['Oldpassword']
        new_pass=request.POST['Newpassword']
        new_verify=request.POST['NewConfirmpassword']
        if(new_pass==new_verify):
            # print(True)
            user=User.objects.get(username=request.session["d_name"])
            # print(user.password)
            check=check_password(current,user.password)
            # print(check)
            if check==True:
                # print(check)
                user1=deliveryboy.objects.get(deliveryboy_name=request.session["d_name"])
                user1.password=new_pass
                user1.save()
                request.session["d_pass"]=new_pass
                user.password=new_pass
                context["message"]="Successfully change password"
                context['color']="alert-success"
                # print(user.password)         
            else:
                context["message"]="Incorrect password"
                context['color']="alert-danger"         
    return render(request,"delivery_boy/change_password.html",context)