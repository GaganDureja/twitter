from django.shortcuts import redirect
from .models import Tweet
from django.contrib import messages


# Create your views here.
def createTweet(request):
  tweet_message = request.POST.get('tweet_message')
  Tweet.objects.create(user = request.user, tweet_message = tweet_message)
  messages.success(request, "Tweet uploaded")
  return redirect('home')