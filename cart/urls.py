from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('chatsend/', views.chatSend, name='chatSend'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),    
    
]