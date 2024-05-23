from django.db import models
from user.models import User
# Create your models here.




class Tweet(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  tweet_message = models.CharField(max_length=160)
  retweet = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
