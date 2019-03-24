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


# @login_required
def home(request,id):
    hood = Neighbourhood.objects.get(id=id)
    return render(request,'home.html',{'hood':hood})

# @login_required
def profile(request,id):
    user = User.objects.get(id=id)
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles':profiles,'user':user}) 

def hood_details(request):
    user = request.user
    if request.method == 'POST':
        hoodform= NeighbourhoodForm(request.POST)
        if hoodform.is_valid():
            hform = hoodform.save(commit=False)
            hform.admin= user
            hform.save()
        return redirect('profile',user.id)
    else:
        hoodform = NeighbourhoodForm()
    return render(request, 'enter_hood.html',{'hoodform':hoodform})

