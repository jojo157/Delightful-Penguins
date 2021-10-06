from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_home, name='artist_home'),
    
]