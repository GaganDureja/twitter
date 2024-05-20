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
  tweet_details = get_object_or_404(Tweet, id=id)
  return render(request, 'tweets/show.html',{'tweet_details':tweet_details})

def editTweet(request,id):
  tweet_details = get_object_or_404(Tweet, id=id)
  if request.user != tweet_details.user:
    messages.error(request, "Invalid path")
    return redirect('home')
  return render(request, 'tweets/edit.html',{'tweet_details':tweet_details})

def updateTweet(request,id):
  tweet_details = get_object_or_404(Tweet, id=id)
  if request.user != tweet_details.user:
    messages.error(request, "Invalid path")
    return redirect('home')
  tweet_details.tweet_message = request.POST.get('tweet_message')
  tweet_details.save()
  messages.success(request, "Tweet updated")
  return redirect('home')