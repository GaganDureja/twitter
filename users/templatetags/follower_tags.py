from django import template

register = template.Library()

@register.filter
def can_follow(user, follow_to):
  if user.id == follow_to.id:
    return False
  if user in follow_to.followers.all():
    return False
  return True

@register.filter
def can_unfollow(user, follow_to):
  if user.id == follow_to.id:
    return False
  if user not in follow_to.followers.all():
    return False
  return True