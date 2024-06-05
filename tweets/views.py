from django.shortcuts import redirect,render, get_object_or_404,HttpResponse
from .models import Tweet
from django.contrib import messages
from django.views import View

# Create your views here.
class TweetView(View):
  def get(self, request, id=None):
    if id is None:
      return redirect('home')
    tweet = get_object_or_404(Tweet, id=id)
    return render(request, 'tweets/show.html',{'tweet':tweet})

  def post(self, request):
    tweet_message = request.POST.get('tweet_message')
    Tweet.objects.create(user = request.user, tweet_message = tweet_message)
    messages.success(request, "Tweet uploaded")
    return redirect('home')


class TweetEditView(View):
  def get(self, request,id):
    tweet = get_object_or_404(Tweet, id=id, user_id=request.user.id)
    if tweet.original_tweet is not None:
      return HttpResponse("Retweets can't be edited", status=422)
    return render(request, 'tweets/edit.html',{'tweet':tweet})

  def post(self, request, id):
    tweet = get_object_or_404(Tweet, id=id, user_id=request.user.id)
    if tweet.original_tweet is not None:
      return HttpResponse("Retweets can't be updated", status=422)
    tweet.tweet_message = request.POST.get('tweet_message')
    tweet.save()
    messages.success(request, "Tweet updated")
    return redirect('tweets:showTweet', id=id)


class TweetDestroyView(View):
  def get(self, request,id):
    tweet = get_object_or_404(Tweet, id=id, user_id=request.user.id)
    tweet.delete()
    messages.success(request, "Tweet deleted")
    return redirect('home')


class RetweetView(View):
  def get(self, request,id):
    tweet = get_object_or_404(Tweet, id=id)
    if request.user.id==tweet.user_id:
      messages.error(request,"Retweets can't be retweeted")
    Tweet.objects.create(user = request.user, original_tweet = tweet)
    messages.success(request, "Tweet Retweeted")
    return redirect('home')