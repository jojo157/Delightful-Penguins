from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers

from chat.views import chatSend
# Create your views here.

def artist_home(request):
    #This function will return the Artist Message page
    #Need to implement only if super user for security
    return render(request, 'artistMessages.html') 


def artist_status(request):
    if request.method == 'POST' and request.is_ajax:
        status = request.POST['status']
        print(status)
        Artist.objects.filter(pk=1).update(status=status)
        response = "success"
        return HttpResponse(status=200)