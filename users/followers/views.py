from django.shortcuts import get_object_or_404
from users.models import User
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
import json


class FollowersViews(View):
  def post(self, request, id):
    user = get_object_or_404(User, id=id)
    if request.user.id==id:
      messages.error(request,'Cannot follow yourself')
      return JsonResponse({'status': 422})
    if request.user.id in id.user.followers:
      messages.error(request,'You are already following')
      return JsonResponse({'status': 422})
    request.user.followers.add(id)
    messages.success(request, "Following now")
    return JsonResponse({'status': 'success'})