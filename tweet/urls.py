from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('add', views.add_tweet, name='add_tweet'),
]
