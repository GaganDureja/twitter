from django import template

register = template.Library()

@register.filter
def is_following(following_user, followed_user):
  if following_user in followed_user.followers.all():
    return False
  return True
