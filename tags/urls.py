from django.urls import path
from . import views
from .followers import views as tagfollowers_views

app_name = 'tags'

urlpatterns = [
  path('', views.TagViews.as_view(), name="TagList"),
  path('<int:id>', views.TagDetailViews.as_view(), name="TagDetails"),
  path('<int:id>/followers', tagfollowers_views.TagFollowersView.as_view(), name='ManageTagFollower'),
]
