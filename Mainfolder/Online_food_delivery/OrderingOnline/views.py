from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth

from OrderingOnline.models import customer,Account_user
from django.contrib.auth.models import User
from Restaurant1.models import restaurant,Item,cart,OrderProduct,Order_confirm
from django.contrib.auth.hashers import check_password

# from OrderingOnline.decoders import unauthenticUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View

from django.views.generic import TemplateView
from django.http import JsonResponse
from django.conf import settings

from decimal import *
import random
import os
from twilio.rest import Client
def save_otp(mobile):
        account_sid = 'AC75173bb622333cb934fbdb95b68e90ce'
        auth_token = 'd2de390e6a58a0df1b39370a63ed0bb6'
        otp=random.randrange(1000,5000)
        client = Client(account_sid, auth_token)
        number='+91'+mobile
        print(number)
        message = client.messages.create(
                body='your otp is {}'.format(otp),
                from_=+12242231053,
                to=+919328003668
        )
        print('otp')
        return otp
        
def index(request):
    context={}
    rest=restaurant.objects.all()
    context['rest']=rest
    context['range']=range(1)
    context['cart_count']=cart.objects.all().count
    return render(request,"OrderingOnline/index.html",context)

def search(request):
    context={}
    context['cart_count']=cart.objects.all().count
    q=request.GET['dish']
    result=Item.objects.filter(pname=q).order_by('feedback','price')
    result2=restaurant.objects.filter(Restaurant_name=q).order_by('feedback')
    context['result']=result
    context['result2']=result2
    print(result)
    return render(request,"OrderingOnline/search.html",context)
    

def about(request):
    context={}
    context['cart_count']=cart.objects.all().count
    return render(request,"OrderingOnline/about.html",context)

def login_category(request):
    return render(request,"OrderingOnline/login_category.html")

def register_category(request):
    return render(request,"OrderingOnline/register_category.html")


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


# logout
@login_required(login_url='/OrderingOnline/login') 
def logout_cutomer(request):
    request.session.flush()
    auth.logout(request)
    return HttpResponseRedirect("/OrderingOnline/login")   
    
# update customer profile 
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
    context['cart_count']=cart.objects.all().count
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
    context['cart_count']=cart.objects.all().count
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

 
def show_dish_by_search(request,id):
    context={}
    context['cart_count']=cart.objects.all().count
    Item_data=Item.objects.get(id=id)
    context['Item_data']=Item_data
    rest=Item_data.rdata.get()
    print(Item_data.id,rest.id)
    context['rest_id']=rest.id
    return render(request,"OrderingOnline/show_dish.html",context)   

# food dish show
def show_dish(request,id,rest_id):
    context={}
    context['cart_count']=cart.objects.all().count
    Item_data=Item.objects.get(id=id)
    context['Item_data']=Item_data
    context['rest_id']=rest_id
    return render(request,"OrderingOnline/show_dish.html",context)


# show restaurnat items
def show_restaurant(request,id):
    context={}
    context['cart_count']=cart.objects.all().count
    items=Item.objects.filter(rdata=id)
    context['items']=items
    context['rest_id']=id
    return render(request,"OrderingOnline/show_restaurant_items.html",context)


@login_required(login_url='/OrderingOnline/login')
def cart_show(request):
    context={}
    cust=customer.objects.get(id=request.session['customer_id'])
    cartuser=cart.objects.filter(userdata=cust)
    context['cart']=cartuser
    price=0.0
    for x in cartuser:
        price+=x.quantity*(float(x.Items_data.price)-float(x.Items_data.discount))
        print(x.Items_data.pname)
    context['price']=price
    return render(request,"OrderingOnline/cart.html",context)

@login_required(login_url='/OrderingOnline/login')
def cart_increase(request,id):
    context={}
    cust=customer.objects.get(id=request.session['customer_id'])
    cartuser=cart.objects.filter(userdata=cust)
    price=0.0
    for x in cartuser:
                price+=x.quantity*(float(x.Items_data.price)-float(x.Items_data.discount))
                print(x.Items_data.pname)
                context['price']=price
    if request.method=='POST':
        print(id)
        context['cart_count']=cart.objects.all().count
        cust=customer.objects.get(id=request.session['customer_id'])
        cartuser=cart.objects.filter(userdata=cust)
        context['cart']=cartuser
        cart_item=cart.objects.get(id=id)
        print(cart_item)
        if request.POST['increase']=='+':
            cart_item.quantity=Decimal((request.POST['quantity']))
            cart_item.save()
            cart_item.final_amount=float(Decimal(cart_item.quantity)*Decimal((cart_item.final_amount)))                                                                                                                                                                                                                                                                                                                           
            cart_item.save()
            price=0.0
            for x in cartuser:
                price+=x.quantity*(float(x.Items_data.price)-float(x.Items_data.discount))
                print(x.Items_data.pname)
                context['price']=price
        return render(request,"OrderingOnline/cart.html",context)
    return render(request,"OrderingOnline/cart.html",context)




   
   
   
#adding data in cart 
@login_required(login_url='/OrderingOnline/login')
def add_to_cart(request,rest_id,id,page):
    context={}
    context['cart_count']=cart.objects.all().count
    Item_data=Item.objects.get(id=id)
    print(Item_data.id)
    cust=customer.objects.get(id=request.session['customer_id'])
    print(cust.id)
    check_data=cart.objects.filter(userdata=cust,Items_data=Item_data)
    print(check_data)
    quantity=1
    if check_data:
        try:
            if page == 'show_restaurant_items':
                messages.info(request,Item_data)
                messages.warning(request, "You have already this dish in cart")
                return HttpResponseRedirect("/OrderingOnline/show_restaurant/{}".format(rest_id))
            if page == 'show_dish':
                messages.info(request,Item_data)
                messages.warning(request, "You have already this dish in cart")
                return HttpResponseRedirect("/OrderingOnline/showdetails/{0},{1}".format(id,rest_id))
        except:
            return HttpResponseRedirect("/OrderingOnline/showdishes/{0}".format(id))
    else:
        final_amount=(float(Item_data.price)-float(Item_data.discount))
        print(final_amount)
        final_amount=float(quantity)*(final_amount)
        cartItem=cart(userdata=cust,Items_data=Item_data,quantity=quantity,final_amount=final_amount)
        cartItem.save() 
    # print(cartItem)
    cartuser=cart.objects.filter(userdata=cust)
    context['cart']=cartuser
    for x in cartuser:
        item=Item.objects.get(id=x.Items_data_id)
        item.total=float(item.price)-float(item.discount)
        item.save()
        print(x.Items_data.pname)
    return HttpResponseRedirect("/OrderingOnline/cartdetails")
  
  
  
    
def add_to_favourite(request,id):
    pass








@login_required(login_url='/OrderingOnline/login')
def placeorder(request):
    context={}
    context['cart_count']=cart.objects.all().count
    user=customer.objects.get(id=request.session['customer_id'])
    cart_data=cart.objects.filter(userdata=user)
    price=0.0
    for x in cart_data:
        price+=x.quantity*(float(x.Items_data.price)-float(x.Items_data.discount))
        print(x.Items_data.pname)
    context['price']=price
    context['cart']=cart_data
    context['confirm']="Do You want to order? "
    if request.method=='POST':
        context['confirm']=''
        for x in cart_data:         # for fetching data from order
            # item=Item.objects.get(id=x.Items_data_id)
            order_place=OrderProduct(price=x.final_amount,userdata=user,cartdata=x)
            order_place.save()
        print(price)
        order=OrderProduct.objects.filter(userdata=user)
        print("order-total ",price)
        context['order']=order
        context['total']=price
        return render(request,"OrderingOnline/confirmation_order.html",context)
    return render(request,"OrderingOnline/cart.html",context)
    




#deleteitems from cart and order
@login_required(login_url='/OrderingOnline/login')
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
    context['cart_count']=cart.objects.all().count
    context['cart_item_success']="successfully deleted"
    cartuser=cart.objects.filter(userdata=user)
    context['cart']=cartuser
    price=0
    for x in cartuser:
        item=Item.objects.get(id=x.Items_data_id)
        item.total=float(item.price)-float(item.discount)
        item.save()
        print(item.total)
        price+=float(item.price)-float(item.discount) 
    context['price']=price 
    return render(request,"OrderingOnline/cart.html",context)


# delete from place order
# @login_required(login_url='/OrderingOnline/login')
# def delete_item_from_order(request,id,order_id):
#     user=customer.objects.get(id=request.session['customer_id'])
#     print("cart-id",id)
#     cartdata=cart.objects.get(id=id)
#     data=OrderProduct.objects.get(id=order_id,cartdata=cartdata,userdata=user.id)
#     data.delete()
#     context={}
#     context['cart_item_success']="successfully deleted"
#     order=OrderProduct.objects.filter(userdata=user)
#     context['order']=order
#     for y in order:
#         price+=float(y.price)
#         print("order-total ",price)
#     context['total']=price
#     return HttpResponseRedirect('/OrderingOnline/placeorder/')

@login_required(login_url='/OrderingOnline/login')
def charge_pay(request):
    return render(request,'OrderingOnline/payment.html')


@login_required(login_url='/OrderingOnline/login')
def payment(request):
    context={}
    if request.method=="POST":
        uname=request.POST['uname']
        account=request.POST['account_no']
        print(uname,account)
        try:
            user_data=customer.objects.get(uname=uname)
            try:  
                user=Account_user.objects.get(user_account=user_data)
                if user:
                    account_user=Account_user.objects.get(account_no=account)
                    print(account_user)
                    otp=save_otp(user_data.mobile)
                    request.session['otp']=otp
                    # print("s1",otp)
                    context['otp']=otp
                else:
                     context['detail']="Account no is wrong"
            except Account_user.DoesNotExist:
                print("no")
                context['not_saved']=['Not saved']
        except:
            context['detail']="Account user is not exist"
    return render(request,'OrderingOnline/payment.html',context)

def saved_account(request):
    context={}
    if request.method=="POST":
        account=request.POST['account_no']
        customer_data=customer.objects.get(id=request.session['customer_id'])
        if customer_data is not None:
            account_user=Account_user(user_account=customer_data,account_no=account,bank_password=0)
            print(account_user)
            account_user.save()
    return render(request,'OrderingOnline/payment.html',context)

def reset_account(request):
    context={}
    context['reset']="reset"
    if request.method=='POST':
         account=request.POST['reset']
         user=customer.objects.get(id=request.session['customer_id'])
         if user:
             account_user=Account_user.objects.get(user_account=user)
             account_user.account_no=account
             account_user.save()
             conetxt['success']="Successfully changed"
         return render(request,'OrderingOnline/payment.html',context)
    return render(request,'OrderingOnline/payment.html',context)
    
    
def final_payment(request):
    context={}
    user=customer.objects.get(id=request.session['customer_id'])
    cart1=cart.objects.filter(userdata=user)
    if request.method == 'POST':
        otp=request.session['otp']
        print("s",otp)
        if otp == request.POST['otp']:
            context['successfully']="successfully ordered"
            for x in cart1:
                order=OrderProduct.objects.filter(cartdata=x,userdata=user)
                order_final=Order_confirm(Item=x.Items_data,price=x.final_amount,quantity=x.quantity)
                order_final.save()
                print(order)
                order.delete()
                x.delete()
            return render(request,"OrderingOnline/order.html",context)
        else:
            context['resend']="resend"
            for x in cart1:
                print("delete")
                order=OrderProduct.objects.filter(cartdata=x,userdata=user)
                order.delete()
            return render(request,'OrderingOnline/order.html',context)
    return render(request,'OrderingOnline/payment.html',context)




#order page current order status:
def orderpage(request):
    context={}
    order=Order_confirm.objects.filter(user=request.session['customer_id'])
    context['order']=order
    return render(request,"OrderingOnline/order.html",context)

# import stripe

# # Create your views here.
    
# # stripe  key
# stripe.api_key = settings.STRIPE_SECRET_KEY

# class product_landing(TemplateView):
#     template_name='OrderingOnline/payment.html'
    
#     def get_context_data(self,**kwargs):
        
#         context=super(product_landing,self).get_context_data(**kwargs)
#         context.update({
#               'STRIPE_PUBLIC_KEY':settings.STRIPE_PUBLIC_KEY
#         })    
#         return context
    
    
    
    
# class CreateCheckoutSessionView(View):
#     def post(self,request,*args,**kwargs):
#         YOUR_DOMAIN = 'http://127.0.0.1:8000'
#         product_id=self.kwargs['pk']
#         product=Item.objects.get(id=product_id)
#         print(product)
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'inr',
#                         'unit_amount': product.price,
#                         'Product_data': {
#                             'name': product.pname,
#                             # 'images': ['https://i.imgur.com/EHyR2nP.png'],
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return JsonResponse({
#             'id': checkout_session.id
#         })
# if __name__ == '__main__':
#     app.run(port=4242)

