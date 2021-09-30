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
            if not request.session.get("ip_address"):
                request.session['ip_address'] = ip
                request.session.modified = True
        if request.user:
            user_name = request.user
        else:
            user_name = 'Guest'
        
        message_content = request.POST['message'] 
        chat_session = ip
        user_name = user_name
         
        new_message = Message(message_content=message_content, chat_session=chat_session, user_name=user_name)
        new_message.save()
        data = get_list_or_404(Message, chat_session=chat_session)
        context = {
            'chat_messages': data,
            'chat_session': chat_session,
        }
        return render(request, 'home.html', context)
    
    if request.method == 'GET':
        if request.session.get("ip_address"): 
            chat_session = ip_address
            data = get_list_or_404(Message, chat_session=chat_session)
            context = {
                'chat_messages': data,
                'chat_session': chat_session,
            }
        return render(request, 'home.html', context)
  


def chat(request):
    data = get_list_or_404(Message, chat_session=request.session['chat_session'])
    context={
        'chat_messages': data, 
    }
    return render(request, 'home.html', context)



