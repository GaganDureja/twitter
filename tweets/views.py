from django.shortcuts import redirect,render, get_object_or_404
from .models import Tweet
from django.contrib import messages


# Create your views here.
def createTweet(request):
  tweet_message = request.POST.get('tweet_message')
  Tweet.objects.create(user = request.user, tweet_message = tweet_message)
  messages.success(request, "Tweet uploaded")
  return redirect('home')

def showTweet(request,id):
  tweet = get_object_or_404(Tweet, id=id)
  return render(request, 'tweets/show.html',{'tweet':tweet})

def editTweet(request,id):
  tweet = get_object_or_404(Tweet, id=id, user_id=request.user.id, original_tweet__isnull=True)
  return render(request, 'tweets/edit.html',{'tweet':tweet})

def updateTweet(request,id):
  tweet = get_object_or_404(Tweet, id=id, user_id=request.user.id, original_tweet__isnull=True)
  tweet.tweet_message = request.POST.get('tweet_message')
  tweet.save()
  messages.success(request, "Tweet updated")
  return redirect('tweets:showTweet', id=id)

def destroyTweet(request,id):
  tweet = get_object_or_404(Tweet, id=id, user_id=request.user.id)
  tweet.delete()
  messages.success(request, "Tweet deleted")
  return redirect('home')

def reTweet(request,id):
  tweet = get_object_or_404(Tweet, id=id)
  if request.user.id==tweet.user_id:
    messages.error(request,'Cannot Retweet self Tweet')
  Tweet.objects.create(user = request.user, original_tweet = tweet)
  messages.success(request, "Tweet Retweeted")
  return redirect('home')