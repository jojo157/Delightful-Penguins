from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('chatSend/', views.chatSend, name='chatSend'),
    path('all_orders/', views.all_orders, name='all_orders'),

    
]
