from django.db import models
from users.models import User
# Create your models here.

class Tag(models.Model):
  name = models.CharField(max_length=160)
  followers =models.ManyToManyField(User)