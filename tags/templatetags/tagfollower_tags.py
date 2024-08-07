from django import template

register = template.Library()

@register.filter
def is_following_tag(user, tag):
  return tag.followers.filter(id=user.id).exists()
