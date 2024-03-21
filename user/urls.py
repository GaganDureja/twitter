from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('signup', views.signup, name='Signup'),
    path('signin', views.signin, name='Signin'),
    path('logout', views.user_logout, name='Logout'),
]
