from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404,
    HttpResponse,
    reverse,
)
from django.contrib import messages
from django.conf import settings
import stripe
from chat.views import (
    chatSend,
    get_ip,
    numberOfMessages,
    chatMessages,
    addNewMessage,
)

from art.models import Art
from .models import Order, OrderLineItem
from .forms import OrderForm
from cart.cart_contexts import cart_contents
from django.views.decorators.http import require_POST

from django.core.mail import send_mail
from django.template.loader import render_to_string
import json


@require_POST
def cache_checkout_data(request):
    """
    This view modifies the payment intent for stripe to include the cart, username and pid
    """
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "cart": json.dumps(request.session.get("cart", {})),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be \
            processed right now. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    This view processes the checkout call,
    when request is POST, it adds order to database 
    when request is get the checkout form is displayed with order summary and stripe intent created
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get("cart", {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()

            for chosen_id in cart.items():
                art = Art.objects.get(id=chosen_id[0])

                order_line_item = OrderLineItem(
                    order=order, art=art, lineitem_total=art.price
                )
                order_line_item.save()
            messages.success(
                request,
                f"Order successfully processed! \
            A confirmation email will be sent to {order.email}.",
            )

            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            messages.error(
                request,
                "There was an error with your form. \
                Please double check your information.",
            )

    else:
        cart = request.session.get("cart", {})

        if not cart:
            messages.error(request, "Your cart is empty")
            return redirect(reverse("art"))

        current_cart = cart_contents(request)
        total = current_cart["total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
        template = "checkout.html"
        context = {
            "order_form": order_form,
            "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
            "client_secret": intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    This view returns checkout success page with order summary
    """
    order = get_object_or_404(Order, order_number=order_number)

    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
