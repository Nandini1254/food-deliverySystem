from django.urls import path
from restaurant import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('r_login/',views.r_login,name="login"),
    path('r_signup/',views.r_signup,name="signup"), 
    path('profile/',views.profile_show,name="profile"), 
    path('update_rest/',views.update,name="updateprofile_rest"), 
    path('logout_rest/',views.logout_rest,name="logout_rest"),
    path('change_password/',views.change_password,name="change_password"),
] 