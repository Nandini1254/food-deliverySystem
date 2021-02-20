from django.urls import path
from OrderingOnline import views
import restaurant.views as views2
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name="logincustomer"),
    path('r_login/',views2.r_login,name="loginrestaurant"),
    path('r_signup/',views2.r_signup,name="restaurantsignup"),
    path('signup/',views.signup,name="customersignup"),
    path('login_category/',views.login_category,name="login_category"),
    path('register_category/',views.register_category,name="register_category"),
    # path('r_login/',restaurant.views.r_login,name="login_restaurnt"),
] 
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
