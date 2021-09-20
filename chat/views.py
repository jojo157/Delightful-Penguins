from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'chatLogin.html')


def chat(request):
    return render(request, 'chatRoom.html')


