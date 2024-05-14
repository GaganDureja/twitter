from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
  path('create', views.createTweet, name='createTweet'),
  path('read/<int:id>', views.readTweet, name='readTweet'),
]
