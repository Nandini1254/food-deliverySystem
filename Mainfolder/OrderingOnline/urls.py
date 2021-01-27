from django.urls import path
from OrderingOnline import views
urlpatterns = [

    path('',views.index,name="index"),
]
