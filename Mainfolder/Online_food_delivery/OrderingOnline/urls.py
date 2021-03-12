from django.urls import path
from OrderingOnline import views
import Restaurant1.views as views2
import delivery_boy.views as views3
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name="logincustomer"),
    path('signup/',views.signup,name="customersignup"),
    path('logout/',views.logout_cutomer,name="logout_customer"),
    path('profile/',views.profile_show_customer,name="profile_customer"),
    path('update/',views.update,name="updateprofile_cust"),
    path('delete/',views.delete_customer,name="delete_customer"),
    path('changepassword/',views.changingpassword_cust,name="changingpassword_customer"),
     
    path('login_category/',views.login_category,name="login_category"),
    path('register_category/',views.register_category,name="register_category"),
#     //restaurant
    path('r_login/',views2.r_login,name="loginrestaurant"),
    path('r_signup/',views2.r_signup,name="restaurantsignup"),
   
    
#     delivery boy
    path('d_login/',views3.d_login,name="logindeliveryboy"),
    path('d_signup/',views3.d_signup,name='deliveryboysignup'),
    
    
    # forget password
     path('resetpassword/', 
         auth_views.PasswordResetView.as_view(template_name='OrderingOnline/forgetpassword.html'),
         name="reset_password"),
    
    path('resetpassworddone/', 
         auth_views.PasswordResetDoneView.as_view(template_name='OrderingOnline/forgetpassword_confirm.html'),
         name="password_reset_done"),
    
    path('resetpasswordconfirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='OrderingOnline/forgetpasswordreset.html'),
         name="password_reset_confirm"),
    
    path('resetpasswordchange/',
         auth_views.PasswordResetCompleteView.as_view(template_name='OrderingOnline/forgetpasswordreset_confirmation.html'),
         name="password_reset_complete"),
    
    
#     showing restaurant data  at user side
     path("show_restaurant/<int:id>/",views.show_restaurant,name="show_restaurant"),
     path("add_to_cart/<int:rest_id>,<int:id>,<slug:page>",views.add_to_cart,name="add_to_cart"),
     path("add_to_favourite/<int:id>/",views.add_to_favourite,name="add_to_favourite"),
     path("cartdetails/",views.cart_show,name="cart_show"),
     path("showdetails/<int:rest_id>,<int:id>/",views.show_dish,name="show_dish"),
     path("deleteitems/<int:id>/",views.delete_item_from_cart,name="delete_item_from_cart"),
     path("placeorder/",views.placeorder,name="placeorder"),
      path("deleteitems_order/<int:id>/",views.delete_item_from_order,name="delete_item_from_order"),
     



]