from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
import json 

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
        return HttpResponse(status=200)


def reply(request, id):
    message = Message.objects.get(pk=id)
    context = {
        'new_chat_message': message.message_content,
        'new_user': message.user_name,
        'new_chat_session': message.chat_session,
        'new_id': id
    }
    return render(request, 'reply.html', context) 

def artist_send_reply(request):
    if request.method == 'POST':
        id = request.POST['message-id']
        old_message = Message.objects.get(pk=id)
        message_content = request.POST['message']
        chat_session = old_message.chat_session
        user_name = "Leticia"
        new_message = Message(message_content=message_content, chat_session=chat_session, user_name=user_name, reply_recieved=True)
        new_message.save()
        Message.objects.filter(pk=id).update(reply_recieved=True)
        messages.success(request, "reply sent")

    return render(request, 'artistMessages.html') 
        