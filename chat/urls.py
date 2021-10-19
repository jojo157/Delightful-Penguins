from django.urls import path
from . import views

urlpatterns = [
    path('chatSend/', views.chatSend, name='chatSend'),
    path('contact/', views.contact, name='contact'),
    path('numberOfMessages/', views.numberOfMessages, name='numberOfMessages'),
    
]
