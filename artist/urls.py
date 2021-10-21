from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.artist_home, name="artist_home"),
    path("artist_status/", views.artist_status, name="artist_status"),
    path("chatSend/", views.chatSend, name="chatSend"),
    path("numberOfMessages/", views.numberOfMessages, name="numberOfMessages"),
    path("reply/<int:id>/", views.reply, name="reply"),
    path("artist_send_reply/", views.artist_send_reply, name="artist_send_reply"),
]
