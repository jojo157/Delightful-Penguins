from django.contrib import admin
from .models import Message, Artist, Contact


admin.site.register(Message)
admin.site.register(Artist)
admin.site.register(Contact)
