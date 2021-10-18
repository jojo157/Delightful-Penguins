from django.contrib import admin
from .models import Message, Artist, Contact
# Register your models here.

admin.site.register(Message)
admin.site.register(Artist)
admin.site.register(Contact)