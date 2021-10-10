from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.art, name='art'),
    path('addArt/', views.addArt, name='addArt'),
    path('editArt/<int:id>/', views.editArt, name='editArt'),
    path('chatSend/', views.chatSend, name='chatSend'), 


]