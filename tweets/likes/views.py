from django.shortcuts import  get_object_or_404
from tweets.models import Tweet
from django.contrib import messages
from django.views import View
from django.http import JsonResponse


class LikeView(View):
  def post(self, request, id):
    tweet = get_object_or_404(Tweet, id=id)
    if request.user.id in tweet.likes.all():
      messages.error(request,"You've already liked this tweet")
      return JsonResponse({'status': 422})
    tweet.likes.add(request.user.id)
    messages.success(request, "Tweet Liked")
    return JsonResponse({'status': 200})

  def delete(self, request, id):
    tweet = get_object_or_404(Tweet, id=id)
    if not tweet.likes.filter(id=request.user.id).exists():
      messages.error(request,"You haven't liked this tweet")
      return JsonResponse({'status': 422})
    tweet.likes.remove(request.user.id)
    messages.success(request, "Like removed")
    return JsonResponse({'status': 200})
