from django.contrib import admin
from .models import Message, Artist, Contact


class MessageAdmin(admin.ModelAdmin):
    
    list_display = (
        "message_content",
        "date_of_message",
        "user_name",
        "chat_session",
        "reply_recieved",
    )


class ArtistAdmin(admin.ModelAdmin):
    
    list_display = (
        "status",
    )

class ContactAdmin(admin.ModelAdmin):
    
    list_display = (
        "title",
        "contact_message",
        "email",
        "mobile",
    )   


admin.site.register(Message, MessageAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Contact, ContactAdmin)
