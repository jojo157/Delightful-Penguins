from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages

import json

# Create your views here.

def chatSend(request):
    #This function will take AJAX Post of a chat message and will call the fuction to add message to the database
    # The message and relevant username will be sent as a response to the AJAX call in json format
    if request.method == 'POST' and request.is_ajax:
        message = request.POST['message'] 
        response = addNewMessage(request, message)
        return HttpResponse(json.dumps(response))


def home(request):
    #hard setting artist status for now, will create a function to deal with this later
    # status will be Offline or Online
    Artist.objects.create(status="Offline")

    #we will remove messages if ip not in session for that ip so chatbox is new everytime user accesses site
    if not 'ip_address' in request.session:
        ip = get_ip(request)
        Message.objects.filter(chat_session=ip).delete()
        return render(request, 'home.html')
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
    # This function adds a new message to the messages model database
    if not request.session.get("ip_address"):
        ip = get_ip(request)
        request.session['ip_address'] = ip
    if request.user.is_authenticated:
        if not request.user.username == "admin" :
            user_name = request.user.username
        else:
            user_name = "Leticia"
    else:
        user_name = 'Guest'
        
    message_content = message
    chat_session = request.session['ip_address']
         
    new_message = Message(message_content=message_content, chat_session=chat_session, user_name=user_name, reply_recieved=False)
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


def artist_available(request):
    Artist.objects.filter(pk=1).update(status="Online")