from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
  path('create', views.TweetView.as_view(http_method_names=['post']), name='createTweet'),
  path('show/<int:id>', views.TweetView.as_view(http_method_names=['get']), name='showTweet'),
  path('edit/<int:id>', views.TweetEditView.as_view(http_method_names=['get']), name='editTweet'),
  path('update/<int:id>', views.TweetEditView.as_view(http_method_names=['post']), name='updateTweet'),
  path('destroy/<int:id>', views.TweetDestroyView.as_view(http_method_names=['get']), name='destroyTweet'),
  path('retweet/<int:id>', views.RetweetView.as_view(http_method_names=['get']), name='reTweet')
]
