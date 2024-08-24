from django.shortcuts import  get_object_or_404
from tweets.models import Tweet
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from .models import Likes


class LikesView(View):
  def post(self, request, id):
    tweet = get_object_or_404(Tweet, id=id)
    Likes.objects.create(user=request.user, tweet=tweet)
    messages.success(request, "Tweet Liked")
    return JsonResponse({'status': 200})

  def delete(self, request, id):
    tweet_like = get_object_or_404(Likes, tweet_id=id, user_id=request.user.id)
    tweet_like.delete()
    messages.success(request, "Like removed")
    return JsonResponse({'status': 200})
