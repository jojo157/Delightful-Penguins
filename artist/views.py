from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json 

from chat.views import chatSend


@login_required
def artist_home(request):
#This function returns the Artist Message page if user is super user (artist)
    if request.user.is_superuser:
        return render(request, 'artistMessages.html') 

@login_required
def artist_status(request):
#This function updates the user status to Offline or Online depending on the status recieved
    if request.user.is_superuser:
        if request.method == 'POST' and request.is_ajax:
            status = request.POST['status']
            print(status)
            Artist.objects.filter(pk=1).update(status=status)
            return HttpResponse(status=200)

@login_required
def reply(request, id):
#This function renders a page with the message details that the artist has choosen to reply to.
    if request.user.is_superuser:
        message = Message.objects.get(pk=id)
        context = {
            'new_chat_message': message.message_content,
            'new_user': message.user_name,
            'new_chat_session': message.chat_session,
            'new_id': id
        }
        return render(request, 'reply.html', context) 


@login_required
def artist_send_reply(request):
#This function adds a reply message to the message the artist replied to.
#The function updates the reply recieved field to True for the message that a reply was sent to
    if request.user.is_superuser:
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
        return redirect('artist_home')   