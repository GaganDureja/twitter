from django import template

register = template.Library()

@register.filter
def can_edit_tweet(user, tweet):
  return user.id == tweet.user_id and tweet.original_tweet is None

@register.filter
def can_delete_tweet(user, tweet):
  return user.id == tweet.user_id

@register.filter
def can_retweet(user, tweet):
  return user.id != tweet.user_id and user.is_authenticated and tweet.original_tweet is None
