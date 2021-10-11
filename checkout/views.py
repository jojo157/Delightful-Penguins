from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, 'Your cart is empty')
        return redirect(reverse('art'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': settings.STRIPE_SECRET_KEY,
    }

    return render(request, template, context)
