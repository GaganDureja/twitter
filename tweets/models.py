from django.db import models
from users.models import User
# Create your models here.




class Tweet(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  tweet_message = models.CharField(max_length=160)
  original_tweet = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
  last_edited_at =models.DateTimeField(null=True)
  likes = models.ManyToManyField(User, related_name='liked_by')
