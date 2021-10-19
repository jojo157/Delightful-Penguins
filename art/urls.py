from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.art, name='art'),
    path('addArt/', views.addArt, name='addArt'),
    path('editArt/<int:id>/', views.editArt, name='editArt'),
    path('deleteArt/<int:id>/', views.deleteArt, name='deleteArt'),
    path('artDetails/<int:id>/', views.artDetails, name='artDetails'),
    path('chatSend/', views.chatSend, name='chatSend'),  
    path('numberOfMessages/', views.numberOfMessages, name='numberOfMessages'), 
    

]

