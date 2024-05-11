from django.shortcuts import render,redirect
from .models import Tweet
from django.contrib import messages
from user.views import home


# Create your views here.
def add_tweet(request):
    tweet_message = request.POST.get('tweet_message')
    Tweet.objects.create(user = request.user, tweet_message = tweet_message)
    messages.success(request, "Tweet uploaded")
    return redirect('home')