from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import auth,User
# # Create your views here.
def auth_view(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)   
            return HttpResponseRedirect('/loginmodule/loggedin/')
        else:
            return HttpResponseRedirect('/loginmodule/login/')
def login_view(request):
    return render(request,'/loginmodule/login.html')
def loggedin(request):
    return render(request,'/loginmodule/loggedin.html',{"fullname":"request.user.username"})
def logout_view(request):
    auth.logout(request)
    return render(request,'/loginmodule/logout.html')
def invalidlogin(request):
    return render(request,'/loginmodule/invalidlogin.html')