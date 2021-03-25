from django.urls import path, include
from . import views

#API
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('', views.BeefWeekAPI.as_view(), name='api'),
    path('token/', obtain_auth_token, name='obtain-token'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
