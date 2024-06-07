from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
  path('create/', views.TweetView.as_view(), {'action': 'create'}, name='createTweet'),
  path('show/<int:id>/', views.TweetView.as_view(), {'action': 'show'}, name='showTweet'),
  path('edit/<int:id>/', views.TweetView.as_view(), {'action': 'edit'}, name='editTweet'),
  path('update/<int:id>/', views.TweetView.as_view(), {'action': 'update'}, name='updateTweet'),
  path('destroy/<int:id>/', views.TweetView.as_view(), {'action': 'destroy'}, name='destroyTweet'),
  path('retweet/<int:id>/', views.TweetView.as_view(), {'action': 'reTweet'}, name='reTweet'),
]
