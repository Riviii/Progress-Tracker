from types import MemberDescriptorType
from django.db import models

# Create your models here.
# class Feature:
#     id: int
#     name: str
#     details: str
#     is_true : bool

class Feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    

class Student(models.Model):
    name=models.CharField(max_length=100)
    uid=models.CharField(max_length=500)
    group=models.CharField(max_length=500)
    Members=models.CharField(max_length=500)
    member1=models.CharField(max_length=500)
    member2=models.CharField(max_length=500)
    member3=models.CharField(max_length=500)
    member4=models.CharField(max_length=500)
    member5=models.CharField(max_length=500)
    member6=models.CharField(max_length=500)
    member7=models.CharField(max_length=500)

    tendays=models.CharField(max_length=500)
    twentydays=models.CharField(max_length=500)
    thirtydays=models.CharField(max_length=500)
    
    