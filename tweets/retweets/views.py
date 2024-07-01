from django.shortcuts import redirect, get_object_or_404
from tweets.models import Tweet
from django.contrib import messages
from django.views import View


class RetweetView(View):
  def post(self, request, original_tweet_id):
    tweet = get_object_or_404(Tweet, id=original_tweet_id)
    if request.user.id==tweet.user_id:
      messages.error(request,'Cannot Retweet self Tweet')
    Tweet.objects.create(user = request.user, original_tweet = tweet)
    messages.success(request, "Tweet Retweeted")
    return redirect('home')