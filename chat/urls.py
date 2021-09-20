from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/<room>', views.chat, name='chat'),
    path('checkroom/', views.checkroom, name='checkroom'),
]
