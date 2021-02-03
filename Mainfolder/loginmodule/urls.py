from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    
     path('login/',views.login_view,name="login"),
     path('logout/',views.logout_view,name="logout"),
     path('loggedin/',views.loggedin,name="logged"),
     path('invalidlogin/',views.invalidlogin,name="login"),
     path('auth_view/',views.auth_view,name="auth"),
]
