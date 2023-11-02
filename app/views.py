from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from app.models import *
from app.forms import *

from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.models import Review
import datetime
def available_maids(request):
    if request.method=='POST':
        se=request.POST['se']
        sti=request.POST['sti']
        eti=request.POST['eti']
        available_maids = Service.objects.filter(Q(service_name=se) & Q(availability_end__gte=sti) & Q(availability_start__lte=eti)).order_by('-rating')
        context = {'available_maids': available_maids}
        return render(request, 'available_maids.html', context)
    return HttpResponse('please first fill maid form')

def available_cooks(request):
    if request.method=='POST':
        se=request.POST['se']
        sti=request.POST['sti']
        eti=request.POST['eti']
        available_cooks = Service.objects.filter(Q(service_name=se) & Q(availability_end__gte=sti) & Q(availability_start__lte=eti)).order_by('-rating')
        context = {'available_cooks': available_cooks}
        return render(request, 'available_cooks.html', context)
    return HttpResponse('please first fill cook form')


def available_nanny(request):
    if request.method=='POST':
        se=request.POST['se']
        sti=request.POST['sti']
        eti=request.POST['eti']
        available_nanny = Service.objects.filter(Q(service_name=se) & Q(availability_end__gte=sti) & Q(availability_start__lte=eti)).order_by('-rating')
        context = {'available_nanny': available_nanny}
        return render(request, 'available_nanny.html', context)
    return HttpResponse('please first fill nanny form')

def available_caretaker(request):
    if request.method=='POST':
        se=request.POST['se']
        sti=request.POST['sti']
        eti=request.POST['eti']
        available_caretaker = Service.objects.filter(Q(service_name=se) & Q(availability_end__gte=sti) & Q(availability_start__lte=eti)).order_by('-rating')
        context = {'available_caretaker': available_caretaker}
        return render(request, 'available_caretaker.html', context)
    return HttpResponse('please first fill caretaker form')

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

@login_required
def booking(request):
    SFO=ServiceForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFOD=ServiceForm(request.POST)
        if SFOD.is_valid():
            SFOD.save()
            return HttpResponse('data is inserted')
            
    return render(request,'services.html',d)

def About(request):
    return render(request,'contact_address_about.html')

def Contact(request):
    return render(request,'contact.html')

@login_required
def nanny(request):
    return render(request,'nanny.html')
@login_required
def maid(request):
    return render(request,'maid.html')

@login_required
def cook(request):
    return render(request,'cook.html')

def care_taker(request):
    return render(request,'care.html')


def registration(request):
    d={'usfo':UserForm(),'pfo':ProfileForm()}
    if request.method=='POST' and request.FILES:
        usfd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if usfd.is_valid() and pfd.is_valid():
            NSUO=usfd.save(commit=False)
            password=usfd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()

            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()

            send_mail('Registration',"Succesfully Registration is Done",'vallepusravani9705@gmail.com',[NSUO.email],fail_silently=False)


            return HttpResponse('Regsitration is Susssessfull')
        else:
            return HttpResponse('Not valid')
    return render(request,'registration.html',d)

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid username or password') 
        
    return render(request,'User_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    
@login_required
def display_profile(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'display_profile.html',d)

@login_required
def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('Password is Changed successfully')
    return render(request,'change_password.html')

def forgot_password(request):
    if request.method=='POST':
        username=request.POST['username']
        pw=request.POST['pw']
        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(pw)
            UO.save()
            return HttpResponse('Password reset is done')
        else:
            return HttpResponse('Username is not valid')
    return render(request,'forgot_password.html') 


def show(request):
        service_list = Service.objects.all().order_by('rating')
        top_service = Service.objects.all().order_by('rating')[:5]
        return render(request, 'booking.html', {'service_list': service_list,'top_service': top_service})

def service_list(request):
    services = Service.objects.all().order_by('rating')
    service_list = []
    service_by_rate = []
    rate= services[0].rating
    for i in range(0, len(services)):
	    if rate != services[i].rating:
             service_list.append(service_by_rate)
             service_by_rate = []
             service_by_rate.append(services[i])
    
    service_list.append(service_by_rate)
     
    return render(request, 'service_list.html', {'services': service_list})  
