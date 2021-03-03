from django.shortcuts import render
# Create your views here.
import filetype
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
from Restaurant1.models import restaurant,Category,Item
# Create your views here.


def home(request):
    return render(request,"Restaurant1/rHome.html")

def r_login(request):
    if request.method=="POST":
       uname=request.POST['email']
       password=request.POST['password']
       user1 = auth.authenticate(username=uname,password=password)
       print(user1)
       if user1 is not None:
           print("yes")
           user=restaurant.objects.get(uname=uname)
           auth.login(request,user1)
           request.session["r_name"]=user.Restaurant_name
           request.session["r_user"]=user.uname
           request.session['r_city']=user.city
           request.session['r_state']=user.state
           request.session['r_address']=user.address
           request.session['r_status']=user.status
           request.session['r_mobile']=user.mobile
           request.session['r_email']=user.email
           print(user.Restaurant_photo)
           request.session['r_photo']=str(user.Restaurant_photo) 
           return render(request,"Restaurant1/rHome.Html")               
       else:
           return HttpResponse(request,"not find")
    else:
        return render(request,'Restaurant1/r_login.html')
def r_signup(request):
    context={}
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
           user1=User.objects.create_user(username=uname,email=email,password=password)
           user=restaurant(Restaurant_name=restname,status=False,uname=uname,email=email,mobile=mobileno,password=cpassword,address=address,state=state,city=city)
           if user is not None:
             if "restphoto" in request.FILES:
                if filetype.is_image(request.FILES['restphoto']):
                    user.Restaurant_photo=request.FILES['restphoto']
                    user.save()
                    user1.save()
                    context['success']=messages="successfully inserted"
                    print(user)
                    return render(request,"Restaurant1/r_login.html")
                else:
                    context['error']="Please enter Image file"          
    return render(request,'Restaurant1/r_register.html',context)
   
def update(request):
    context={}
    context['error']=''
    context['success']=''
    if request.method=="POST":
       restname=request.POST['restname']
       restphoto=''
       mobileno=request.POST['mobileno']
       address=request.POST['address']
       state=request.POST['state']
       city=request.POST['city']  
       email=request.session['r_email']
       if restaurant.objects.filter(email=email).exists():
           user=restaurant.objects.get(email=email)
           if user is not None:          
               user.Restaurant_name=restname
               user.mobileno=mobileno
               user.state=state
               user.city=city
               user.address=address
               if "restphoto" in request.FILES:
                   if filetype.is_image(request.FILES['restphoto']):
                         user.Restaurant_photo=request.FILES['restphoto']
                         user.save()
                         context['success']=messages="successfully inserted"
                         request.session['r_photo']=str(user.Restaurant_photo)
                   else:
                        context['error']="Please enter Image file"
               #  print(request.session['r_photo'])
               request.session["r_name"]=user.Restaurant_name
               request.session["r_user"]=user.uname
               request.session['r_city']=user.city
               request.session['r_state']=user.state
               request.session['r_address']=user.address
               request.session['r_mobile']=user.mobile 
               
               return render(request,'Restaurant1/profile.html',context)
           else:
               return render(request,"/")
    else:
        return render(request,'Restaurant1/profile.html')
# to show profile      
def profile_show(request):   
    return render(request,"Restaurant1/profile.html")

def logout_rest(request):
    request.session.flush()
    auth.logout(request)
    return HttpResponseRedirect("/restaurant/r_login")

# change password
def changingpassword(request):
    context={}
    if request.method=='POST':
        current=request.POST['Oldpassword']
        new_pass=request.POST['Newpassword']
        new_verify=request.POST['NewConfirmpassword']
        if(new_pass==new_verify):
            # print(True)
            user=User.objects.get(username=request.session["r_user"])
            # print(user.password)
            check=check_password(current,user.password)
            # print(check)
            if check==True:
                # print(check)
                user1=restaurant.objects.get(uname=request.session["r_user"])
                user1.password=new_pass
                user1.save()
                request.session["r_pass"]=new_pass
                user.password=new_pass
                context["success"]="Successfully change password"
                context['color']="alert-success"
                # print(user.password)         
            else:
                context["fail"]="Incorrect password"
                context['color']="alert-danger"         
    return render(request,"Restaurant1/changingpassword.html",context)


#add item in resaturant
def add_items(request):
    context={}
    cat=Category.objects.all()
    context['cat']=cat
    if request.method=="POST":
        rdata=restaurant.objects.get(uname=request.session['r_user'])
        print(rdata)
        food=request.POST['foodname']
        category=request.POST.getlist('category',None)
        desc=request.POST['desc']
        price=request.POST['price']
        image=request.FILES['foodphoto']
        if filetype.is_image(image):
            data_item=Item(pname=food,pdesc=desc,price=price,pimage=image,category=category[0])
            data_item.save()
            data_item.rdata.add(rdata)
            # data_get=Item.objects.get(pname=food)
            # print(data_get['id']) 
            context['success']="Successfully added"
        else:
            context['error']="Please enter Image file"           
    return render(request,"Restaurant1/additems.html",context)


def manageitems(request):
    context={}
    data=Item.objects.all()
    print("dt")
    print(data)
    context['data']=data
    return render(request,"Restaurant1/manage_items.html",context)

def itemdetails(request,id):
    context={}
    data=Item.objects.get(id=id)
    data_category=Category.objects.all()
    print(data_category)
    context['data_category']=data_category
    context['data']=data
    return render(request,"Restaurant1/itemdetails.html",context)




