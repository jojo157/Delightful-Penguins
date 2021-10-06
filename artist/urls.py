from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.artist_home, name='artist_home'),
    path('artist_status/', views.artist_status, name='artist_status'), 
    path('chatSend/', views.chatSend, name='chatSend'), 

]