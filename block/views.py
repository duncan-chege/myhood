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
    biz = Business.objects.filter(bizhood=hood.id)       #returns an array. That's why we for loop
    return render(request,'home.html',{'hood':hood,'biz':biz,'user':user})
    
def biz_details(request):
    user = request.user
    hood = Neighbourhood.objects.get(admin=user)        #returns one object
    print(hood)

    if request.method == 'POST':
        bizform= BusinessForm(request.POST)
        if bizform.is_valid():
            bform = bizform.save(commit=False)
            bform.person= user      #foreign key
            bform.bizhood= hood      #foreign key
            bform.save()
        return redirect('home', hood.id)
    else:
        bizform = BusinessForm()
    return render(request, 'enter_biz.html',{'bizform':bizform})

def search_results(request):
    if 'business'in request.GET and request.GET['business']:
        user = request.user
        name = request.GET.get("business")
        searched_businesses = Business.search_by_bizname(name)
        message = f'{name}'

        return render(request, 'search.html',{'message':message, 'businesses': searched_businesses,'user':user})

            






