from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json 
from chat.views import chatSend
from .forms import ArtForm
from .models import Art

# Create your views here.

def art(request):
    artCollection = Art.objects.all()
    context={
        'artCollection': artCollection
    }
    return render(request, 'art.html', context)


def addArt(request):
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save()
            messages.success(request, "Art added")
            return redriect(request,'art')
    else:
        form = ArtForm()
        context= {
            'form': form,
        }
        return render(request, 'artAdd.html', context)  