from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=254, unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)    
    verified_account = models.BooleanField(default=False)
    profile_imgg = models.FileField(upload_to="profile", null=True, blank=True)
    bg_imgg = models.FileField(upload_to="profile", null=True, blank=True)
    followers = models.ManyToManyField('user.User')

    