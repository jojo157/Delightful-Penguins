from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from django.contrib import messages
from django.conf import settings
import stripe

from art.models import Art
from .models import Order, OrderLineItem
from .forms import OrderForm
from cart.cart_contexts import cart_contents


# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()

            for chosen_id in cart.items():
                art = Art.objects.get(id=chosen_id[0])
                

                order_line_item = OrderLineItem(
                    order=order,
                    art=art,
                    lineitem_total=art.price
                )
                order_line_item.save()
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart = request.session.get('cart', {})

        if not cart:
            messages.error(request, 'Your cart is empty')
            return redirect(reverse('art'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        print(intent)

        order_form = OrderForm()
        template = 'checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
