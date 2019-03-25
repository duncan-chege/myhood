from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()     #will hash the password fro security
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    user= request.user
    profiles = Profile.objects.all()
    hood = Neighbourhood.objects.filter(admin=user.id)
    return render(request, 'profile.html', {'profiles':profiles,'user':user,'hood':hood}) 

def hood_details(request):
    user = request.user
    if request.method == 'POST':
        hoodform= NeighbourhoodForm(request.POST)
        if hoodform.is_valid():
            hform = hoodform.save(commit=False)
            hform.admin= user
            hform.save()
        return redirect('profile')
    else:
        hoodform = NeighbourhoodForm()
    return render(request, 'enter_hood.html',{'hoodform':hoodform})

# @login_required
def home(request,id):
    user = request.user
    hood = Neighbourhood.objects.get(id=id)
    return render(request,'home.html',{'hood':hood,'user':user})

def biz_details(request):
    user = request.user
    if request.method == 'POST':
        bizform= BusinessForm(request.POST)
        if bizform.is_valid():
            bform = bizform.save(commit=False)
            bform.admin= user
            bform.save()
        return redirect('home')
    else:
        bizform = BusinessForm()
    return render(request, 'enter_biz.html',{'bizform':bizform})



            






