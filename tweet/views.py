from django.shortcuts import redirect,render, get_object_or_404
from .models import Tweet
from django.contrib import messages


# Create your views here.
def createTweet(request):
  tweet_message = request.POST.get('tweet_message')
  Tweet.objects.create(user = request.user, tweet_message = tweet_message)
  messages.success(request, "Tweet uploaded")
  return redirect('home')

def readTweet(request,id):
  tweet_details = get_object_or_404(Tweet, id=id)
  return render(request, 'tweet/tweet-detail.html',{'tweet_details':tweet_details})