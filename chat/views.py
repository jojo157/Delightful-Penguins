from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse
from chat.models import Message

import json

# Create your views here.


def home(request):
   # credit to ArRosid for code to obtain users IP address
   # https://medium.com/@arrosid/how-to-get-visitor-ip-address-in-django-project-793d383969ae
    if request.method == 'POST':
        #credit for this code to ArRosid
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        #end of credit for this code
            if not request.session['ip_address']: 
                request.session['ip_address'] = ip
        if request.user:
            user_name = request.user
        else:
            user_name = 'Guest',
        data = {
            message_content : request.POST['message'],
            chat_session : request.session['ip_address'],
            user_name : user_name,
        }
        Message.objects.create(data)
    
    else:    
        if request.session['ip_address']: 
            ip = request.session['ip_address']
            data = Message.objects.get(chat_session=ip)
            context = {
                'ip_address': ip, 
                'messages': data,
            }
        else:
            context = {}
    return render(request, 'home.html', context)


def chat(request):
    data = get_list_or_404(Message, chat_session=request.session['chat_session'])
    context={
        'chat_messages': data, 
    }
    return render(request, 'home.html', context)



