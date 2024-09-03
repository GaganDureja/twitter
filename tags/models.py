from django.db import models
from tags.followers.models import tagsFollowers
# Create your models here.

class Tag(models.Model):
  name = models.CharField(max_length=160)