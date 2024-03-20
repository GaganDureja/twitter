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

    # return redirect('home') if request.user.is_authenticated else render(request,'tweet/index.html')
    # if request.user.is_authenticated:
    #     return redirect('home')
    # return render(request,'tweet/index.html')


def home(request):
    if request.user.is_authenticated:
        return render(request,'tweet/home.html')
    return redirect('index')

    # return render(request,'tweet/home.html') if request.user.is_authenticated else redirect('index')
    # if request.user.is_authenticated:
    #     return render(request,'tweet/home.html')
    # return redirect('index')

def signup(request):
    if request.user.is_authenticated or request.method == 'GET':
        return redirect('index')
    # first name and last name
    email = request.POST.get('email')
    name = request.POST.get('name')
    password = make_password(request.POST.get('password'))
    try:
        user = User.objects.create(username=email, password=password)
        messages.success(request, "Login to continue")
    except Exception as e:
        messages.error(request, e )

    # user, created = User.objects.create(
    #     password = password,
    #     username = email,
    #     first_name = name,
    #     email=email
    # )
    # if not created:
    #     messages.error(request, "Error")
    # else:
    #     messages.success(request, "Login to continue")
    return redirect('index')




def signin(request):
    if request.method == 'GET' or request.user.is_authenticated:
        return redirect('index')

    unique_identity = request.POST.get('email')
    password = request.POST.get('password')
    select_user = User.objects.filter(email=unique_identity)

    if not select_user:
        messages.warning(request, "Account not found")
        return redirect('index')

    unique_identity = select_user.first().username
    user = authenticate(request,username=unique_identity,password=password)

    if not user:
        messages.error(request, "Incorrect password!!!")
        return redirect('index')

    login(request, user)
    return redirect('index')
    # if request.user.is_authenticated:
    #     return redirect('index')
    # else:
    #     if request.method == 'GET':
    #         return redirect('index')

    #     if request.method == 'POST':
    #         unique_identity = request.POST.get('email')
    #         password = request.POST.get('password')

    #         if User.objects.filter(Q(email=unique_identity) | Q(phone=unique_identity) | Q(username=unique_identity)):
    #             unique_identity = User.objects.filter(Q(email=unique_identity) | Q(phone=unique_identity) | Q(username=unique_identity)).first().username
    #             user = authenticate(
    #                     request,
    #                     username=unique_identity,
    #                     password=password
    #                 )
    #             if user:
    #                 login(request, user)
    #             else:
    #                 messages.error(request, "Incorrect password!!!")
    #         else:
    #             messages.warning(request, "Account not found")
    #     return redirect('index')

def user_logout(request):
    # if request.user.is_authenticated:
    logout(request)
    return redirect('index')
