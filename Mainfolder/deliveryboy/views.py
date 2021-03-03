from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import auth
from deliveryboy.models import deliveryboy_manager
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
# Create your views here.


def home(request):
    return render(request,"deliveryboy/d_Home.html")

def d_login(request):
    if request.method=="POST":
       email=request.POST['email']
       password=request.POST['password']
       if deliveryboy_manager.objects.filter(email=email,password=password).exists():
           user=deliveryboy_manager.objects.get(email=email,password=password)
           request.session["d_name"]=user.deliveryboy_name
           request.session["d_user"]=user.uname
           request.session['d_city']=user.city
           request.session['d_state']=user.state
           request.session['d_address']=user.address
           request.session['d_status']=user.status
           request.session['d_mobile']=user.mobile
           request.session['d_email']=user.email
           return render(request,"deliveryboy/d_home.Html")
       else:
           return HttpResponse("not find")
    else:
        return render(request,'deliveryboy/d_login.html')
def d_signup(request):
    if request.method=="POST":
       deliveryboy_name=request.POST['deliveryboy_name']
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
           user=deliveryboy_manager( deliveryboy_name=deliveryboy_name,status=False,uname=uname,email=email,mobile=mobileno,password=cpassword,address=address,state=state,city=city,zipcode=zipcode)
           print(user)
           if user is not None:

               user.save()
               return render(request,"deliveryboy/d_login.html")
       else:
           return HttpResponse("something went wrong")
    else:
        return render(request,'deliveryboy/d_register.html')
    
# Create your views here.
def update(request):
    if request.method=="POST":
       deliveryboy_name=request.POST['deliveryboy_name']
       uname=request.POST['username']
       mobileno=request.POST['mobileno']
       address=request.POST['address']
       state=request.POST['state']
       city=request.POST['city']
       email=request.session['d_email']
       if deliveryboy_manager.objects.filter(email=email).exists():
           user=deliveryboy_manager.objects.get(email=email)
           if user is not None:          
               user.deliveryboy_name=deliveryboy_name
               user.uname=uname
               user.mobileno=mobileno
               user.state=state
               user.city=city
               user.address=address
               request.session["d_name"]=user.deliveryboy_name
               request.session["d_user"]=user.uname
               request.session['d_city']=user.city
               request.session['d_state']=user.state
               request.session['d_address']=user.address
               request.session['d_mobile']=user.mobile 
               user.save()
               messages="successfully inserted"
               return render(request,'deliveryboy/profile.html',{"mess":messages})
           else:
               return HttpResponse("something went wrong")
    else:
        return render(request,'deliveryboy/profile.html')
       
def profile_show(request):
    return render(request,"deliveryboy/profile.html")

def logout_deliveryboy(request):
    if request.session['email']:
        request.session.flush()
    return HttpResponseRedirect("/deliveryboy/d_login")
def change_password(request):
    context={}
    if request.method=='POST':
        current=request.POST['Oldpassword']
        new_pass=request.POST['Newpassword']
        new_verify=request.POST['NewConfirmpassword']
        if(new_pass==new_verify):
            user=User.objects.get(id=request.user.id)
            check=check_password(current,request.user.password)
            if check==True:
                print(check)
                context["message"]="Successfully change password"
                context['color']="alert-success"
                user.set_password(new_pass)          
            else:
                context["message"]="Incorrect password"
                context['color']="alert-danger"         
    return render(request,"deliveryboy/change_password.html",context)
