from django.db import models
from users.models import User
# Create your models here.




class tagsFollowers(models.Model):
  tag = models.ForeignKey('tags.Tag',on_delete=models.CASCADE)
  user = models.ForeignKey(User,on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['tag', 'user'], name='unique_user_tag_follow')
    ]
