from django import template

register = template.Library()

@register.filter
def can_edit_tweet(user, tweet):
  if user.id != tweet.user_id:
    return False
  if tweet.original_tweet_id is not None:
    return False
  return True

@register.filter
def can_delete_tweet(user, tweet):
  return user.id == tweet.user_id

@register.filter
def can_retweet(user, tweet):
  if tweet.original_tweet_id is not None:
    return False
  if not user.is_authenticated:
    return False
  if user.id == tweet.user_id:
    return False
  return True
