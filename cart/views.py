from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404,
)
from art.models import Art
from chat.models import Message
from chat.views import (
    chatSend,
    get_ip,
    numberOfMessages,
    chatMessages,
    addNewMessage,
)
from django.contrib import messages
from django.http import HttpResponseRedirect


def view_cart(request):
    # this view will show the user any art pieces they added to cart

    return render(request, "cart.html")


def add_to_cart(request, id):
    # this view will add the art piece to the cart
    # the cart will be stored in session storage

    art = get_object_or_404(Art, pk=id)

    cart = request.session.get("cart", {})
    cart[id] = id
    messages.success(request, f"Added {art.name} to your cart")
    request.session["cart"] = cart
    return redirect(view_cart)


def remove_cart_item(request, id):
    # This view removes the selected item from the users cart

    art = get_object_or_404(Art, pk=id)
    cart = request.session.get("cart", {})
    del cart[str(id)]
    messages.success(request, f"Removed {art.name} from your cart")
    return redirect(view_cart)
