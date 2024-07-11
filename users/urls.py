from django.urls import path
from . import views
from .followers import views as followers_views

app_name = 'users'

urlpatterns = [
  path('<int:id>', views.UserViews.as_view(), name="UserDetails"),
  path('<int:id>/followers', followers_views.FollowersViews.as_view(), name='ManageFollower'),
  path('registrations/new', views.newRegistration, name='newRegistration'),
  path('registrations/create', views.createRegistration, name='createRegistration'),
  path('sessions/new', views.newSession, name='newSession'),
  path('sessions/create', views.createSession, name='createSession'),
  path('logout', views.user_logout, name='Logout'),
]
