from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import auth
from restaurant.models import Restaurant_manager
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    return render(request,"restaurant/rHome.html")

def r_login(request):
    if request.method=="POST":
       email=request.POST['email']
       password=request.POST['password']
       user1 = auth.authenticate(email=email,password=password)
       if user1 is not None:
           print("yes")
       if Restaurant_manager.objects.filter(email=email).exists():
             user=Restaurant_manager.objects.get(email=email)
             print(user)
        #    auth.login(request,user1)
        #    request.session["r_name"]=user.Restaurant_name
        #    request.session["r_user"]=user.uname
        #    request.session['r_city']=user.city
        #    request.session['r_state']=user.state
        #    request.session['r_address']=user.address
        #    request.session['r_status']=user.status
        #    request.session['r_mobile']=user.mobile
        #    request.session['r_email']=user.email
        #    print(user.Restaurant_photo)
        #    request.session['r_photo']=str(user.Restaurant_photo)
             return render(request,"restaurant/rHome.Html")
       else:
           return HttpResponse("not find")
    else:
        return render(request,'restaurant/r_login.html')
def r_signup(request):
    if request.method=="POST":
       restname=request.POST['restname']
       restphoto=''
       uname=request.POST['username']
       email=request.POST['email']
       mobileno=request.POST['mobileno']
       cpassword=request.POST['password']
       password=request.POST['cpassword']
       address=request.POST['address']
       state=request.POST['state']
       city=request.POST['city']
       if cpassword==password:
           user1=User.objects.Create(email=email,password=password)
           user1.save()
           user=Restaurant_manager(user=user1, Restaurant_name=restname,status=False,uname=uname,email=email,mobile=mobileno,password=cpassword,address=address,state=state,city=city)
           if user is not None:
             if "restphoto" in request.FILES:
                 user.Restaurant_photo=request.FILES['restphoto']
                 user.save()
                 return render(request,"restaurant/r_login.html")
       else:
           return HttpResponse("something went wrong")
    else:
        return render(request,'restaurant/r_register.html')
   
def update(request):
    if request.method=="POST":
       restname=request.POST['restname']
       restphoto=''
       uname=request.POST['username']
       mobileno=request.POST['mobileno']
       address=request.POST['address']
       state=request.POST['state']
       city=request.POST['city']  
       email=request.session['r_email']
       if Restaurant_manager.objects.filter(email=email).exists():
           user=Restaurant_manager.objects.get(email=email)
           if user is not None:          
               user.Restaurant_name=restname
               user.uname=uname
               user.mobileno=mobileno
               user.state=state
               user.city=city
               user.address=address
               if "restphoto" in request.FILES:
                 user.Restaurant_photo=request.FILES['restphoto']
                 user.save()
                 request.session['r_photo']=str(user.Restaurant_photo)
                 user.save()
                 print(request.session['r_photo'])
               request.session["r_name"]=user.Restaurant_name
               request.session["r_user"]=user.uname
               request.session['r_city']=user.city
               request.session['r_state']=user.state
               request.session['r_address']=user.address
               request.session['r_mobile']=user.mobile 
               messages="successfully inserted"
               return render(request,'restaurant/profile.html',{"mess":messages})
           else:
               return HttpResponse("something went wrong")
    else:
        return render(request,'restaurant/profile.html')
       
def profile_show(request):
    return render(request,"restaurant/profile.html")

def logout_rest(request):
    request.session.flush()
    auth.logout(request)
    return HttpResponseRedirect("/restaurant/r_login")


def change_password(request):
    return HttpResponseRedirect("/restaurant/change_password.html")