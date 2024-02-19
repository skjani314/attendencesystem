from django.db import models

# Create your models here.

class clss(models.Model):
    sclass=models.CharField(max_length=10)
    sub=models.CharField(max_length=10)
    tid=models.CharField(max_length=10)
    

class teacher(models.Model):
    tid=models.CharField(max_length=10)
    tname=models.CharField(max_length=20)
    sub=models.CharField(max_length=10)
    dep=models.CharField(max_length=10)

class student(models.Model):
    sid=models.CharField(max_length=10)
    sname=models.CharField(max_length=30)
    sclass=models.CharField(max_length=10)
    roll=models.IntegerField()
    dep=models.CharField(max_length=10)
    year=models.CharField(max_length=10)


class att(models.Model):
     sid=models.CharField(max_length=10)
     sclass=models.CharField(max_length=10)
     sub=models.CharField(max_length=10)
     sub_total=models.IntegerField()
     sub_attended=models.IntegerField()

class regi(models.Model): 
    sid=models.CharField(max_length=10)
    sub=models.CharField(max_length=10)
    tm=models.DateField()
    period=models.IntegerField()
    

   

class tsa(models.Model):
     tid=models.CharField(max_length=10)
     sub=models.CharField(max_length=10)
     sclass=models.CharField(max_length=10)
     tm=models.DateField()
     period=models.IntegerField()
         

