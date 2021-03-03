from django.urls import path
from deliveryboy import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('d_login/',views.d_login,name="login"),
    path('d_signup/',views.d_signup,name="signup"), 
    path('profile_show/',views.profile_show,name="profile"), 
    path('update/',views.update,name="updateprofile_deliveryboy"), 
    path('logout_deliveryboy/',views.logout_deliveryboy,name="logout_deliveryboy"),
    path('change_password/',views.change_password,name="change_password"),
] 
