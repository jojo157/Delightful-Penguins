from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers

import json

# Create your views here.

def chatSend(request):
    
    if request.method == "POST":
        #credit for this code to ArRosid
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        #end of credit for this code
        if not request.session.get("ip_address"):
            request.session['ip_address'] = ip
            request.session.modified = True
        if request.user:
            user_name = request.user
        else:
            user_name = 'Guest'
        
        message_content = request.POST.get('chatmessage')
        chat_session = ip
        user_name = user_name
         
        new_message = Message(message_content=message_content, chat_session=chat_session, user_name=user_name)
        new_message.save()

        data = get_list_or_404(Message, chat_session=chat_session)
        artist_status = Artist.objects.get(pk=1)
        context = {
                'chat_messages': data,
                'artist_status': artist_status,
        }
    return HttpResponse("Success")


def home(request):
    #hard setting artist status for now, will create a function to deal with this later

    Artist.objects.filter(pk=1).update(status="Offline")
    if request.method == 'POST':
        addNewMessage(request)
        context = chatMessages(request)
        return render(request, 'home.html', context)
    else:
        context = chatMessages(request)
        return render(request, 'home.html', context)

  


def chatMessages(request):
    # This function will get the currently stored messages for a particular ip address and the artists status and return these.
    artist_status = Artist.objects.get(pk=1)
    if 'ip_address' in request.session:
        chat_session = request.session['ip_address']
        data = get_list_or_404(Message, chat_session=chat_session)
        context = {
            'chat_messages': data,
            'artist_status': artist_status,
        }
    else:
        context = {
            'artist_status': artist_status,
        }
    return context

def addNewMessage(request):
    # This function adds the new message from the form to the messages model 
    if not request.session.get("ip_address"):
        ip = get_ip(request)
        request.session['ip_address'] = ip
    if request.user:
        user_name = request.user
    else:
        user_name = 'Guest'
        
    message_content = request.POST['message'] 
    chat_session = request.session['ip_address']
    user_name = user_name
         
    new_message = Message(message_content=message_content, chat_session=chat_session, user_name=user_name)
    new_message.save()
    saved = True
    return saved

def get_ip(request):
# credit to ArRosid for code to obtain users IP address
# https://medium.com/@arrosid/how-to-get-visitor-ip-address-in-django-project-793d383969ae
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip