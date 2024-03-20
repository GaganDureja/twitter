from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password
import random
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout



def check_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,'tweet/index.html')


def home(request):
    if request.user.is_authenticated:
        return render(request,'tweet/home.html')
    return redirect('index')


def signup(request):
    if request.user.is_authenticated or request.method == 'GET':
        return redirect('index')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = make_password(request.POST.get('password'))
    try:
        user = User.objects.create(username=email, password=password, first_name=first_name, last_name=last_name)
        messages.success(request, "Login to continue")
    except Exception as e:
        messages.error(request, e)

    return redirect('index')


def signin(request):
    if request.method == 'GET' or request.user.is_authenticated:
        return redirect('index')

    email = request.POST.get('email')
    password = request.POST.get('password')
    select_user = User.objects.filter(username=email)

    if not select_user:
        messages.warning(request, "Account not found")
        return redirect('index')

    user = authenticate(request,username=email,password=password)

    if not user:
        messages.error(request, "Incorrect password!!!")
        return redirect('index')

    login(request, user)
    return redirect('index')


def user_logout(request):
    logout(request)
    return redirect('index')
