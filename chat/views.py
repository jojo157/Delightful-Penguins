from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from art.models import Art

import json

# Create your views here.

def chatSend(request):
    #This function will take AJAX Post of a chat message and will call the fuction to add message to the database
    # The message and relevant username will be sent as a response to the AJAX call in json format
    if request.method == 'POST' and request.is_ajax:
        message = request.POST['message'] 
        response = addNewMessage(request, message)
        return HttpResponse(json.dumps(response))

  
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


def contact(request):
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'mobile': request.POST['mobile'],
            'title': request.POST['title'],
            'contact_message': request.POST['contact_message'],  
        }

        subject = form_data['title']
        body = render_to_string('contact.txt',
        {'form_data': form_data, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        cust_email = form_data['email']

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        ) 

        artCollection = Art.objects.all()
        context ={
            'artCollection': artCollection
        }

        messages.success(request, 'I have recieved your email and will respond shortly')
        return render(request, 'art.html', context)

    else:   
        contact_form = ContactForm()
        template = 'contact.html'
        context = {
                'contact_form': contact_form,
        }

        return render(request, template, context)


def numberOfMessages(request):
    if request.method == 'POST' and request.is_ajax:
        numberOfChatMessagesDisplayed = request.POST['numOfChats'] 
        checkDatabase = chatMessages(request)
        if checkDatabase['chat_messages']:
            currentCount = len(checkDatabase['chat_messages'])
        return HttpResponse(json.dumps(currentCount))