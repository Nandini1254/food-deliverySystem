from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('addrecord',views.addrecord,name="addrecord"),
    path('viewrecord',views.viewrecord,name="view"),
    path('addrecordpage',views.addrecordpage,name="view"),
]