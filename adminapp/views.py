from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from myapp.models import Customer,Enquiry,Login



# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminhome(request):
    couenq=Enquiry.objects.all().count()
    coucust=Customer.objects.all().count()
    coureg=Login.objects.all().count()
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            return render(request,"adminhome.html",locals())
    except KeyError:
        return redirect("crmapp:login")
def logout(request):
    try:
        del request.session["adminid"]
        return redirect("myapp:login")
    except KeyError:
        return redirect("myapp:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewcustomers(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            cust=Customer.objects.all()
            return render(request,"viewcustomers.html",locals())
    except KeyError:
        return redirect("crmapp:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewenquiries(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            enq=Enquiry.objects.all()
            return render(request,"viewenquiries.html",locals())
    except KeyError:
        return redirect("myapp:login")
def delenq(request,id):
    Enquiry.objects.get(id=id).delete()
    return redirect("adminapp:viewenquiries")

def changepassword(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            return render(request,"changepassword.html",locals())
    except KeyError:
        return redirect("myapp:login")
