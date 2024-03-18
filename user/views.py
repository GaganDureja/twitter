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
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET':
            return redirect('index')
        if request.method == 'POST':
            email = request.POST.get('email')
            if not email:
                messages.warning(request, "Email required")
                return redirect('index')
            if User.objects.filter(email=email):
                messages.warning(request, "User already exists with this email")
                return redirect('index')

            full_name = request.POST.get('name')
            full_username = "".join(full_name.split())
            user_name = full_username

            while User.objects.filter(username=user_name).exists():
                random_number = random.randint(1, 9999)
                user_name = f"{full_username}{random_number}"
            User.objects.create(
                password = make_password(request.POST.get('password')),
                username = user_name,
                first_name = full_name,
                email=email
            )
            messages.success(request, "Login to continue")
            return redirect('index')





def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET':
            return redirect('index')

        if request.method == 'POST':
            unique_identity = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(Q(email=unique_identity) | Q(phone=unique_identity) | Q(username=unique_identity)):
                unique_identity = User.objects.filter(Q(email=unique_identity) | Q(phone=unique_identity) | Q(username=unique_identity)).first().username
                user = authenticate(
                        request,
                        username=unique_identity,
                        password=password
                    )
                if user:
                    login(request, user)
                else:
                    messages.error(request, "Incorrect password!!!")
            else:
                messages.warning(request, "Account not found")
        return redirect('index')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
