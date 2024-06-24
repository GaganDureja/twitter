from django.urls import path
from . import views as tweets_views
from .retweets import views as retweets_views
app_name = 'tweets'

urlpatterns = [
  path('create/', tweets_views.TweetsViews.as_view(), {'action': 'create'}, name='createTweet'),
  path('show/<int:id>/', tweets_views.TweetsViews.as_view(), {'action': 'show'}, name='showTweet'),
  path('edit/<int:id>/', tweets_views.TweetsViews.as_view(), {'action': 'edit'}, name='editTweet'),
  path('update/<int:id>/', tweets_views.TweetsViews.as_view(), {'action': 'update'}, name='updateTweet'),
  path('destroy/<int:id>/', tweets_views.TweetsViews.as_view(), {'action': 'destroy'}, name='destroyTweet'),
  path('<int:original_tweet_id>/retweet/', retweets_views.RetweetView.as_view(), name='reTweet'),
]
