from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_home, name='artist_home'),
    path('artist_status/', views.artist_status, name='artist_status'),  
]