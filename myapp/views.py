
from django.shortcuts import render, redirect
from . models import Enquiry,Customer,Login
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.views.decorators.cache import cache_control
# Create your views here.

def registration(request):
    if request.method=="POST":
        name=request.POST["name"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        contactno=request.POST["contactno"]
        emailaddress=request.POST["emailaddress"]
        password=request.POST["password"]
        regdate=datetime.datetime.today()
        cust=Customer(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,regdate=regdate)
        cust.save()
        log=Login(userid=emailaddress,password=password,usertype="customer")
        log.save()
        return render(request,"registration.html",{"msg":"Registration is done"})
    return render(request,"registration.html")

def login(request):
    if request.method=="POST":
        userid=request.POST["userid"]
        password=request.POST["password"]
        try:
            obj=Login.objects.get(userid=userid,password=password)
            if obj is not None:
                    if obj.usertype=='customer':
                        request.session["userid"]=userid
                        return redirect("myapp:search")
                    elif obj.usertype=='admin':
                        request.session["adminid"]=userid
                        return redirect("adminapp:adminhome")
        except ObjectDoesNotExist:
            msg="Invalid User"
        return render(request,"login.html",{"msg":msg})
    return render(request,"login.html")
def search(request):
    names=Customer.objects.all()
    if request.method=="POST":
        loc=request.POST['q']
        val = str(loc) + ".html"
        return render(request,val)
    return render(request,"search.html",locals())

def manali(request):
    return render(request, 'manali.html')

def varanasi(request):
    return render(request, 'varanasi.html')

def explore(request):
    return render(request,"explore.html")
def glossary(request):
    return render(request,"glossary.html")
def chat(request):
    return render(request,"chat.html")
def index(request):
    if request.method=="POST":
        name=request.POST["name"]
        contactno=request.POST["contactno"]
        emailaddress=request.POST["emailaddress"]
        message=request.POST["message"]
        posteddate=datetime.datetime.today()
        enq=Enquiry(name=name,contactno=contactno,emailaddress=emailaddress,message=message,posteddate=posteddate)
        enq.save()
        return render(request,"index.html",{"msg":"Enquiry is saved"})
    return render(request,"index.html")

def aboutus(request):
    return render(request, 'aboutus.html')