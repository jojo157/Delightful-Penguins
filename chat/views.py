from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers

import json

# Create your views here.

def chatSend(request):
    return HttpResponse("Success")


def home(request):
    #hard setting artist status for now, will create a function to deal with this later
    # status will be Offline or Online
    #Artist.objects.create(status="Offline")
    Artist.objects.filter(pk=1).update(status="Online")
    if request.method == 'POST' and request.is_ajax:
        message = request.POST['message'] 
        response = addNewMessage(request, message)
        return HttpResponse(json.dumps(response))
    else:
        return render(request, 'home.html')

  


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

def addNewMessage(request, message):
    # This function adds the new message from the form to the messages model 
    if not request.session.get("ip_address"):
        ip = get_ip(request)
        request.session['ip_address'] = ip
    if request.user.is_authenticated:
        user_name = request.user.username
    else:
        user_name = 'Guest'
        
    message_content = message
    chat_session = request.session['ip_address']
         
    new_message = Message(message_content=message_content, chat_session=chat_session, user_name=user_name)
    new_message.save()
    data = {
       'message_content': message_content,
       'user_name': user_name
    }
    return data

def get_ip(request):
# credit to ArRosid for code to obtain users IP address
# https://medium.com/@arrosid/how-to-get-visitor-ip-address-in-django-project-793d383969ae
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip