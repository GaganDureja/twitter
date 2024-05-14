from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
  path('create', views.createTweet, name='createTweet'),
]
