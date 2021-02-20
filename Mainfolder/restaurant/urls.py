from django.urls import path
from restaurant import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('r_login/',views.r_login,name="login"),
    path('r_signup/',views.r_signup,name="signup"), 
] 