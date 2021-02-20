from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.
def viewrecord(request):
    ob=Student.objects.all()
    print(ob)
    return render(request,'cruidapp/student_list.html',{'object1':ob})
def addrecordpage(request):
    return render(request,'cruidapp/addrecord.html')
def addrecord(request): 
    if request.method=="POST":
        name=request.POST['studentname']
        dob=request.POST['birthdate']
        user=Student(user_name=name,dob=dob)
        if user is not None:
               user.save()
               return render(request,"cruidapp/addinfo.html")
        else:
           return HttpResponse("not added")
    return HttpResponse("no")   
       
     