from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterUserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login success"))
            return redirect('home')
        else:
            messages.success(request, ("Login failed.  Please try again...\n\
                                       If you have forgotten your password then ask Jiun to reset it"))
            return redirect('login')       
    else:
        return render(request, 'authenticate/login.html',
                  {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully Logged Out."))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            messages.success(request, ("Registration successful - awaiting Admin approval"))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form': form,})



