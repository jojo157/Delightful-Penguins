from .models import Message, Artist
from django.shortcuts import get_object_or_404, get_list_or_404


def get_messages(request):
    """
    If an ip address is in session,
    This function returns the messages associated with that ip address,
    in date order and the artists status. 
    """
    if not Artist.objects.filter(pk=1).exists():
        Artist.objects.create(pk=1, status="Offline")

    artist_status = Artist.objects.get(pk=1)
    if "ip_address" in request.session:
        chat_session = request.session["ip_address"]
        data = Message.objects.filter(chat_session=chat_session).order_by(
            "date_of_message"
        )
        context = {
            "chat_messages": data,
            "artist_status": artist_status,
        }
    else:
        context = {
            "artist_status": artist_status,
        }
    return context
