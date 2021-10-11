from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from art.models import Art

def cart_contents(request):
    cart_count = 0
    cart_items = []
    total = 0
    cart = request.session.get('cart', {})

    for id in cart.items():
        art = get_object_or_404(Art, pk=id)
        total += art.price
        cart_count += 1
        cart_items.append({
            'id': id,
            'art': art
        })
    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_count': cart_count,
    }