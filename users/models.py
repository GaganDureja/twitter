from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  email = models.CharField(max_length=254, unique=True)
  followers =models.ManyToManyField('users.User')