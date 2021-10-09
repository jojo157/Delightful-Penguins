from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.art, name='art'),
    path('addArt/', views.addArt, name='addArt'),


]