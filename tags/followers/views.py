from django.shortcuts import  get_object_or_404
from tags.models import Tag
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
# Create your views here.

class TagFollowersView(View):
  def post(self, request, id):
    tag = get_object_or_404(Tag, id=id)
    if request.user.id in tag.followers.all():
      messages.error(request,"You are already following this tag")
      return JsonResponse({'status': 422})
    tag.followers.add(request.user.id)
    messages.success(request, "Following Tag now")
    return JsonResponse({'status': 200})

  def delete(self, request, id):
    tag = get_object_or_404(Tag, id=id)
    if not tag.followers.filter(id=request.user.id).exists():
      messages.error(request,"You haven't followed this Tag")
      return JsonResponse({'status': 422})
    tag.followers.remove(request.user.id)
    messages.success(request, "Unfollowing now")
    return JsonResponse({'status': 200})