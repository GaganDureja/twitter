from django.db import models
from users.models import User
# Create your models here.




class Likes(models.Model):
  tweet = models.ForeignKey('tweets.Tweet',on_delete=models.CASCADE)
  user = models.ForeignKey(User,on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['tweet', 'user'], name='unique_user_tweet_like')
    ]
