from .models import Message, Artist
from django.shortcuts import get_object_or_404, get_list_or_404


def get_messages(request):
    artist_status = Artist.objects.get(pk=1)
    if 'ip_address' in request.session:
        chat_session = request.session['ip_address']
        data = get_list_or_404(Message.objects.order_by('date_of_message'), chat_session=chat_session)
        context = {
            'chat_messages': data,
            'artist_status': artist_status,
        }
    else:
        context = {
            'artist_status': artist_status,
        }
    return context

