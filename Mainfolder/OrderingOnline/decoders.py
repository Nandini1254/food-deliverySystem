from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticUser(func):
    def check_user(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return HttpResponse("hello")
    return check_user