from django.shortcuts import render, redirect

# Create your views here.




def check_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,'tweet/index.html')


def home(request):
    if request.user.is_authenticated:        
        return render(request,'tweet/home.html')
    return redirect('index')