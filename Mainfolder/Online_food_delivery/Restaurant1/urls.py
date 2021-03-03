from django.urls import path
from Restaurant1 import views
urlpatterns = [
    path('home/',views.home,name="r_home"),
    path('r_login/',views.r_login,name="login"),
    path('r_signup/',views.r_signup,name="signup"), 
    path('profile/',views.profile_show,name="profile"), 
    path('update_rest/',views.update,name="updateprofile_rest"), 
    path('logout_rest/',views.logout_rest,name="logout_rest"),
    path('changingpassword/',views.changingpassword,name="changingpassword"),
    path('additems/',views.add_items,name="additems"),
    path('manageitems/',views.manageitems,name="manageitems"),
    path('item_details/<int:id>/',views.itemdetails,name="item_details"),
] 