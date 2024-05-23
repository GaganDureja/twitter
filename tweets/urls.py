from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
  path('create', views.createTweet, name='createTweet'),
  path('show/<int:id>', views.showTweet, name='showTweet'),
  path('edit/<int:id>', views.editTweet, name='editTweet'),
  path('update/<int:id>', views.updateTweet, name='updateTweet'),
  path('destroy/<int:id>', views.destroyTweet, name='destroyTweet'),
]
