from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def artist_home(request):
    return render(request, 'artistMessages.html') 