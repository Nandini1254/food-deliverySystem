from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth
from OrderingOnline.models import customer
from django.contrib.auth.models import User
from Restaurant1.models import restaurant,Item,cart
from django.contrib.auth.hashers import check_password
# from OrderingOnline.decoders import unauthenticUser
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context={}
    rest=restaurant.objects.all()
    context['rest']=rest
    context['range']=range(1)
    return render(request,"OrderingOnline/index.html",context)

def about(request):
    return render(request,"OrderingOnline/about.html")

def login_category(request):
    return render(request,"OrderingOnline/login_category.html")

def register_category(request):
    return render(request,"OrderingOnline/register_category.html")

def login_after_base(request):
    return render(request,"OrderingOnline/login_after_base.html")

def login(request):
    context={}
    if request.method=="POST":
       username=request.POST['email']
       password=request.POST['password']
       user = auth.authenticate(username=username,password=password)
       if user is not None:
            if customer.objects.filter(uname=username).exists():
                user1=customer.objects.get(uname=username)
                print("yes")
                if user1 is not None:
                    auth.login(request,user)
                    request.session['customer_id']=user1.id
                    request.session['user_id']=user.id
                    return render(request,"OrderingOnline/index.html")
                else:
                    context['not_exist'] ="User is not exist"
                    return render(request,'OrderingOnline/login.html',context)
            else:
                context['not_exist'] ="User is not exist"
                return render(request,'OrderingOnline/login.html',context)                
    return render(request,'OrderingOnline/login.html',context)
       
    
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
       if cpassword==password:
           user1=auth.authenticate(username=uname,password=password)
           print(user1)
           if user1 is None:
                print("no")
                user1=User.objects.create_user(username=uname,email=email,password=password)
                if user1 is not None:
                    user=customer(uname=uname,email=email,mobile=mobileno,password=cpassword,address=address,state=state,city=city)
                    if user is not None:
                        print("yes")
                        user1.save()
                        user.save()
                        return render(request,"OrderingOnline/login.html")
                    else:
                        return render(request,"OrderingOnline/register.html")
                else:
                    return render(request,'OrderingOnline/register.html')
       else:
          return render(request,'OrderingOnline/register.html')
    return render(request,'OrderingOnline/register.html')
    
@login_required(login_url='/OrderingOnline/login')  
def profile_show_customer(request):
    context={}
    user=customer.objects.get(id=request.session['customer_id'])
    context['user']=customer.objects.get(id=request.session['customer_id'])
    print(request.session['customer_id'])
    # user=customer.objects.get(id=request.session['customer_id'])
    # print(user)  
    return render(request,"OrderingOnline/profile.html",context)

@login_required(login_url='/OrderingOnline/login') 
def logout_cutomer(request):
    request.session.flush()
    auth.logout(request)
    return HttpResponseRedirect("/OrderingOnline/login")   
    
    
@login_required(login_url='/OrderingOnline/login')
def update(request):
    context={}
    user=customer.objects.get(id=request.session['customer_id'])
    context['user']=customer.objects.get(id=request.session['customer_id'])
    if request.method=="POST":     
       if restaurant.objects.filter(id=request.session['customer_id']).exists():
           user=customer.objects.get(id=request.session['customer_id'])
           print("yes")
           if user is not None:          
               user.mobileno=request.POST['mobileno']
               user.state=request.POST['state']
               user.city=request.POST['city']
               user.address=request.POST['address']    
               user.save() 
               context['success']="successfully updated"        
               return render(request,'OrderingOnline/profile.html',context)
           else:
               return render(request,"/OrderingOnline/signup")
    else:
        return render(request,'OrderingOnline/profile.html',context)
  
  
#delete account
@login_required(login_url='/OrderingOnline/login')
def delete_customer(request):
    context={}
    user=customer.objects.get(id=request.session['customer_id'])
    context['user']=customer.objects.get(id=request.session['customer_id'])
    context['sure']="Are you sure? Do you want to account delete? "
    if request.method=='POST':
        delete=request.POST['yes']
        if delete is not None:
            cust=customer.objects.get(id=request.session['customer_id'])
            user=User.objects.get(username=cust.uname)
            data=cart.objects.filter(userdata=cust)     
            data.delete()
            user.delete()
            cust.delete()
            request.session.flush()
            auth.logout(request)
            context['sure']=''
            return render(request,"OrderingOnline/index.html") 
                  
    return render(request,'OrderingOnline/index.html',context)

  
# change password
@login_required(login_url='/OrderingOnline/login')
def changingpassword_cust(request):
    context={}
    if request.method=='POST':
        current=request.POST['Oldpassword']
        new_pass=request.POST['Newpassword']
        new_verify=request.POST['NewConfirmpassword']
        if(new_pass==new_verify):
            user=User.objects.get(id=request.session['user_id'])
            check=check_password(current,user.password)
            # print(check)
            if check==True:
                # print(check)
                user1=customer.objects.get(id=request.session['customer_id'])
                user1.password=new_pass
                user1.save()
                user.set_password(new_pass)
                user.save()
                print(user.password)
                context["success"]="Successfully change password"      
            else:
                context["fail"]="Incorrect password"    
        else:
            context['not_same']="password is not same"    
    return render(request,"OrderingOnline/changingpassword.html",context)

    

# show restaurnat items
@login_required(login_url='/OrderingOnline/login')
def show_restaurant(request,id):
    context={}
    items=Item.objects.filter(rdata=id)
    context['items']=items
    return render(request,"OrderingOnline/show_restaurant_items.html",context)


def cart_show(request):
    context={}
    cust=customer.objects.get(id=request.session['customer_id'])
    cartuser=cart.objects.filter(userdata=cust)
    context['cart']=cartuser
    return render(request,"OrderingOnline/cart.html",context)
    
    
def add_to_cart(request,id):
    context={}
    Item_data=Item.objects.get(id=id)
    cust=customer.objects.get(id=request.session['customer_id'])
    cartItem=cart(userdata=cust,Items_data=Item_data,quantity=1)
    cartItem.save()
    # print(cartItem)
    cartuser=cart.objects.filter(userdata=cust)
    context['cart']=cartuser
    for x in cartuser:
        print(x.Items_data.pname)
    return HttpResponseRedirect("/OrderingOnline/cartdetails")
    
def add_to_favourite(request,id):
    pass
    
    
def show_dish(request,id):
    context={}
    Item_data=Item.objects.get(id=id)
    context['Item_data']=Item_data
    return render(request,"OrderingOnline/show_dish.html",context)

def delete_item_from_cart(request,id):
    user=customer.objects.get(id=request.session['customer_id'])
    Item_data=Item.objects.get(id=id)
    data=cart.objects.get(Items_data=Item_data,userdata=user)
    Item_deleted_id=data.return_items_id()
    print(data.Items_data)
    print(data.userdata)
    print(Item_deleted_id)
    data.delete()
    context={}
    context['cart_item_success']="successfully deleted"
    return render(request,"OrderingOnline/cart.html",context)