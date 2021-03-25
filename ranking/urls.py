from django.urls import path, include
from . import views

#API
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home),
    path('play/', views.new_player, name='play'),
]
