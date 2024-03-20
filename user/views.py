from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout





def home(request):
    if request.user.is_authenticated:
        return render(request,'tweet/home.html')
    return render(request,'tweet/login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        return render(request,'tweet/register.html')


    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = make_password(request.POST.get('password'))
    try:
        User.objects.create(username=email, password=password, first_name=first_name, last_name=last_name)
        messages.success(request, "Login to continue")
    except Exception as e:
        messages.error(request, e)
    return redirect('home')


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        return render(request,'tweet/login.html')


    email = request.POST.get('email')
    password = request.POST.get('password')
    select_user = User.objects.filter(username=email)

    if not select_user:
        messages.warning(request, "Account not found")
        return redirect('home')

    user = authenticate(request,username=email,password=password)
    if not user:
        messages.error(request, "Incorrect password!!!")
        return redirect('home')

    login(request, user)
    return redirect('home')


def user_logout(request):
    logout(request)
    return redirect('home')
