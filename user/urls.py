from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
  path('<int:id>', views.UserViews.as_view(), name="UserDetails"),
  path('registrations/new', views.newRegistration, name='newRegistration'),
  path('registrations/create', views.createRegistration, name='createRegistration'),
  path('sessions/new', views.newSession, name='newSession'),
  path('sessions/create', views.createSession, name='createSession'),
  path('logout', views.user_logout, name='Logout'),
]
