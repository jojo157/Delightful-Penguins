from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404,
    HttpResponse,
    reverse,
)
from checkout.models import Order, OrderLineItem
from chat.views import chatSend

from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profiles(request):
    """
    This view returns the orders associated with the users email.
    """
    user = request.user.email
    orders = Order.objects.filter(email=user).order_by('-date')
    context = {
        "orders": orders,
    }
    return render(request, "orders.html", context)


@login_required
def all_orders(request):
    """
    This view renders all orders stored.
    Only a super user can access this page.
    """
    if request.user.is_superuser:
        orders = Order.objects.filter().order_by('-date')
        context = {
            "orders": orders,
        }
        return render(request, "orders.html", context)
