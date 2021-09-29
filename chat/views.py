from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from chat.models import ChatSession, Message

# Create your views here.


def home(request):
   # credit to ArRosid for code to obtain users IP address
   # https://medium.com/@arrosid/how-to-get-visitor-ip-address-in-django-project-793d383969ae
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    request.session['ip_address'] = ip
    context={
        'ip_address': ip, 
    }
    return render(request, 'home.html', context)


def chat(request):
    data = get_list_or_404(Message, chat_session=request.session['chat_session'])
    context={
        'chat_messages': data, 
    }
    return render(request, 'home.html', context)



