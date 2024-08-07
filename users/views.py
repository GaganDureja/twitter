from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from django.http import Http404
from tweets.models import Tweet
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views import View


def home(request):
  all_tweets = Tweet.objects.all().order_by('-id')
  page = request.GET.get('page', 1)
  paginator = Paginator(all_tweets, 10)
  try:
    tweets = paginator.page(page)
  except (PageNotAnInteger, EmptyPage):
    tweets = paginator.page(1)
  return render(request,'home.html', {'all_tweets': tweets})

class UserViews(View):
  def get(self, request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'users/show.html',{'user':user})

def newRegistration(request):
  if request.user.is_authenticated:
    return redirect('home')
  return render(request,'users/register.html')

def createRegistration(request):
  if request.method != 'POST':
    raise Http404("Page not found")
  if request.user.is_authenticated:
    return redirect('home')
  email = request.POST.get('email')
  username = email.split("@")[0]
  first_name = request.POST.get('first_name')
  last_name = request.POST.get('last_name')
  password = make_password(request.POST.get('password'))
  try:
    User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
    messages.success(request, "Login to continue")
  except Exception as e:
    messages.error(request, e)
  return redirect('home')

def newSession(request):
  if request.user.is_authenticated:
    return redirect('home')
  return render(request,'users/login.html')

def createSession(request):
  if request.method != 'POST':
    raise Http404("Page not found")
  if request.user.is_authenticated:
    return redirect('home')
  email = request.POST.get('email')
  username = email.split("@")[0]
  password = request.POST.get('password')
  select_user = User.objects.filter(username=username)

  if not select_user:
    messages.warning(request, "Account not found")
    return redirect('home')

  user = authenticate(request,username=username,password=password)
  if not user:
    messages.error(request, "Incorrect password!!!")
    return redirect('home')

  login(request, user)
  return redirect('home')

def user_logout(request):
  logout(request)
  return redirect('home')