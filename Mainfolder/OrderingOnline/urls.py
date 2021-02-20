from django.urls import path
from OrderingOnline import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    
] 
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
