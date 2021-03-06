from django.urls import path
from OrderingOnline import views
import Restaurant1.views as views2
import delivery_boy.views as views3
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name="logincustomer"),
    path('r_login/',views2.r_login,name="loginrestaurant"),
    path('r_signup/',views2.r_signup,name="restaurantsignup"),
    path('login_after_base/',views.login_after_base,name="userlogin"),
    path('signup/',views.signup,name="customersignup"),
    path('login_category/',views.login_category,name="login_category"),
    path('register_category/',views.register_category,name="register_category"),
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
    
]