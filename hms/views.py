from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def view_home(request):
    resp=render(request,'hms/home.html')
    return resp


def view_about(request):
    resp=render(request,'hms/about.html')
    return resp

def view_timeline(request):
    resp=render(request,'hms/timeline.html')
    return resp

def view_healthspecialist(request):
    resp=render(request,'hms/healthspecialist.html')
    return resp

def view_testimonials(request):
    resp=render(request,'hms/testimonials.html')
    return resp

def view_contact(request):
    resp=render(request,'hms/contact.html')
    return resp

def view_login(request):
    if request.method=='GET':
        resp=render(request,'hms/login.html')
        return resp
    elif request.method=='POST':
        u_username=request.POST.get('t1','N.A')
        u_password=request.POST.get('p1','N.A')
        u=authenticate(request=request,username=u_username,password=u_password)
        if u is not None:
            login(request,user=u)
            resp=render(request,'hms/home.html')
            return resp
        else:
            resp=render(request,'hms/login.html')
            return resp


def view_logout(request):
    logout(request=request)
    resp=render(request,'hms/home.html')
    return resp



@login_required(login_url='login')
def view_booking(request):
    if request.method=='GET':
        frm_unbound= BookingForm()
        dict={'forms':frm_unbound}
        resp=render(request,'hms/booking.html',context=dict)
        return resp
    elif request.method=='POST':
        frm_bound=BookingForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp=HttpResponse('<h1>RESPONSE STORED SUCCESSFULLY!!!</h1>')
            return resp
            


def view_registeration(request):
    if request.method=="GET":
        frm_unbound=UserCreationForm()
        dict={'forms':frm_unbound}
        resp=render(request,'hms/registeration.html',context=dict)
        return resp
    elif request.method=="POST":
        frm_bound=UserCreationForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp=render(request,'hms/home.html')
            return resp
        else:
            dict={"forms":frm_bound}
            resp=render(request,'hms/registeration.html',context=dict)
            return resp






