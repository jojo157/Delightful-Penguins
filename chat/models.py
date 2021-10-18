from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):
    message_content = models.CharField(max_length=1000000)
    date_of_message = models.DateTimeField(default=datetime.now, blank=True)
    user_name = models.CharField(max_length=100)
    chat_session = models.GenericIPAddressField()
    reply_recieved = models.BooleanField(default=False)

class Artist(models.Model):
    status = models.CharField(max_length=1000000)


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    mobile = models.CharField(max_length=20, null=False, blank=False)
    title = models.CharField(max_length=10000)
    contact_message = models.CharField(max_length=1000000)

    


