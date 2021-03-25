from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ranking.urls'), name='ranking'),
    path('api/', include('api.urls'), name='api'),

]
