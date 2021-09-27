from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from chat.models import Room, Message

# Create your views here.


def home(request):
    return render(request, 'chatLogin.html')


def chat(request, room):
    data = get_list_or_404(Message, room_name=room)
    context={
        'chat_messages': data, 
    }
    return render(request, 'chatRoom.html', context)


def checkroom(request):
    room_name = request.POST["room"]
    user_name = request.POST["username"]

    if Room.objects.filter(room_name=room_name).exists():
        return redirect('/chat/'+room_name)
    else:
        new_room = Room.objects.create(room_name=room_name)
        new_room.save
        return redirect('/chat/'+room_name)


