from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('chatSend/', views.chatSend, name='chatSend'), 
    path('numberOfMessages/', views.numberOfMessages, name='numberOfMessages'), 
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'), 
]