from django import template
from tags.followers.models import tagsFollowers
register = template.Library()

@register.filter
def is_following_tag(user, tag):
  return tagsFollowers.objects.filter(user=user,tag=tag).exists()
