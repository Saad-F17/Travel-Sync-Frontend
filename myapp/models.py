from django.db import models

# Create your models here.
class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)
    message=models.CharField(max_length=5000)
    posteddate=models.CharField(max_length=30)
class Customer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=500)
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50,primary_key=True)
    regdate=models.CharField(max_length=30)




    