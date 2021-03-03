from django.urls import path
from delivery_boy import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('d_login/',views.d_login,name="logindeliveryboy"),
    path('d_signup/',views.d_signup,name="deliveryboysignup"), 
    path('profile_show/',views.profile_show,name="d_profile"), 
    path('update/',views.update,name="updateprofile_deliveryboy"), 
    path('logout_deliveryboy/',views.logout_deliveryboy,name="logout_deliveryboy"),
    path('change_password/',views.change_password,name="change_password"),
]