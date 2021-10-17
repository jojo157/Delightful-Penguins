from django.urls import path
from . import views

urlpatterns = [
    path('chatSend/', views.chatSend, name='chatSend'),
]
