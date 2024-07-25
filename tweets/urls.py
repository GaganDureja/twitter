from django.urls import path
from . import views as tweets_views
from .retweets import views as retweets_views
from .likes import views as likes_views
app_name = 'tweets'

urlpatterns = [
  path('', tweets_views.TweetsViews.as_view(), name='ListCreateTweets'),
  path('<int:id>', tweets_views.TweetDetailViews.as_view(), name='ManageTweet'),
  path('<int:id>/edit', tweets_views.TweetDetailViews.as_view(), {'action': 'edit'}, name='editTweet'),
  path('<int:original_tweet_id>/retweet/', retweets_views.RetweetView.as_view(http_method_names=['post']), name='reTweet'),
  path('<int:id>/likes', likes_views.LikesView.as_view(), name='LikeTweet'),
]
