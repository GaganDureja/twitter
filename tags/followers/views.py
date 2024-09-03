from django.shortcuts import  get_object_or_404
from tags.models import Tag
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from tags.followers.models import tagsFollowers
# Create your views here.

class TagFollowersView(View):
  def post(self, request, id):
    tag = get_object_or_404(Tag, id=id)
    tagsFollowers.objects.create(user=request.user, tag=tag)
    messages.success(request, "Following Tag now")
    return JsonResponse({'status': 200})

  def delete(self, request, id):
    tag_following = get_object_or_404(tagsFollowers, tag_id=id, user_id=request.user.id)
    tag_following.delete()
    messages.success(request, "Unfollowing now")
    return JsonResponse({'status': 200})