from django.db import models

# Create your models here.
from user.models import User





class Hashtags(models.Model):
    name = models.TextField(max_length=255, unique=True)
    used_times = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)


class T_Media(models.Model):
    file_name = models.FileField(upload_to="tweets")




class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    msg = models.TextField(max_length=10000, null=True, blank=True)
    REPLY_TYPES = (
        (0,'Everyone'),
        (1,'Accounts you follow'),
        (2,'Verified'),
        (3,'Only accounts mention')
    )
    reply_by = models.IntegerField(default=0, choices=REPLY_TYPES)
    mentions = models.ManyToManyField('user.User', related_name='mentioned_in_tweets', null=True, blank=True)
    tweet_media =models.ManyToManyField(T_Media)
    tweet_hashtag =models.ManyToManyField(Hashtags, null=True, blank=True)

    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    total_comments = models.IntegerField(default=0)   
    repost_tweet = models.ForeignKey('self', on_delete=models.CASCADE, related_name='repost_tweets', null=True, blank=True)
    total_reposts = models.IntegerField(default=0)
    likes = models.ManyToManyField('user.User', related_name='liked_by', null=True, blank=True)
    total_likes = models.IntegerField(default=0)
    views = models.ManyToManyField('user.User', related_name='viewed_by', null=True, blank=True)
    total_views = models.IntegerField(default=0)    

    active_status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


