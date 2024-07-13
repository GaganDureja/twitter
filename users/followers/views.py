from django.shortcuts import get_object_or_404
from users.models import User
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
import json


class FollowersViews(View):
  def post(self, request, id):
    follow_to_user = get_object_or_404(User, id=id)
    if request.user.id==id:
      messages.error(request,'Cannot follow yourself')
      return JsonResponse({'status': 422})
    if request.user.id in follow_to_user.followers.all():
      messages.error(request,'You are already following')
      return JsonResponse({'status': 422})
    follow_to_user.followers.add(request.user.id)
    messages.success(request, "Following now")
    return JsonResponse({'status': 200})

  def delete(self, request, id):
    unfollow_to_user = get_object_or_404(User, id=id)
    if request.user.id==id:
      messages.error(request,'Cannot unfollow yourself')
      return JsonResponse({'status': 422})
    if not unfollow_to_user.followers.filter(id=request.user.id).exists():
      messages.error(request,'You are not following')
      return JsonResponse({'status': 422})
    unfollow_to_user.followers.remove(request.user.id)
    messages.success(request, "Unfollowing now")
    return JsonResponse({'status': 200})