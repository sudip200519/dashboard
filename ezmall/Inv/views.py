from django.shortcuts import render
from django.http import HttpResponse
from .models import person_collection
from .models import Courses,Buy,Student


# Create your views here.

def dashboard(request):
    Buy=Buy.objects.all()
    Student=Student.objects.all()
    total_student=Buy.count()
    Enrolled=Buy.filter(status='Enrolled').count()
    Pending=Buy.filter(status='Pending').count()
    
    context={
        'orders':Buy,
        'Students':Student,
        'Total_student':total_student,
        'Enrolled':Enrolled,
        'pending':Pending,
    }
    return render(request,'dashboard.html',context)

def Courses(request):
    item=Courses.objects.all()
    context={
        'item':item
    }
    return render(request,'courses.html',context)

def Student(request,pk_test):
    Student=Student.objects.get(id=pk_test)
    Buy=Student.Buy_set.all()
    Buy_Count=Buy.count()
    
    context={
        'pk_test':pk_test,'Student':Student,'Buy':Buy,'Buy_Count':Buy_Count
    }
    
    return render(request,'student.html',{'pk_test':pk_test})

#database work start

def index(request):
    return HttpResponse("<h1>app is runing</h1>")

def add_person(request): 
    records={
        "first_name":"SARSS",
        "last_name":"DLMS",
    }
    person_collection.insert_one(records)
    return HttpResponse("successfully added")

def get_all_person(request):
    Inv=person_collection.find()
    return (Inv)

def catch_all_view(request):
    return HttpResponse("Catch-all: This wasn't matched by other URL patterns.")
