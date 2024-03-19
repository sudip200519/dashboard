from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=10,null=True)
    email=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self) :
        return self.name

class Tags(models.Model):
    name=models.CharField(max_length=50,null=True)
    
    def __str__(self) :
            return self.name

class Courses(models.Model):
    CATEGORY=(
        ('Avaliable','Available'),
        ('Unavailable','Unavailable'),
    )
    
    name=models.CharField(max_length=50,null=True)
    price=models.FloatField()
    category=models.CharField(max_length=50,null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,null=True)
    date_created=models.DateField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tags)
    
    def __str__(self) :
            return self.name

class Buy(models.Model):
    STATUS=(
        ('pending','Pending'),
        ('Service_closed','service_closed'),
        ('You_Have_Enrolled','You_Have_Enrolled')
        
    )
    Student=models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    Courses=models.ForeignKey(Courses,null=True,on_delete=models.SET_NULL)
    date_created=models.DateField(auto_now_add=True,null=True)
    Status=models.CharField(max_length=50,null=True,choices=STATUS)
    
    
    
