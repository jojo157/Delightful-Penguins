from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, reverse
from checkout.models import Order, OrderLineItem

from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profiles(request):
    user = request.user.email
    orders = Order.objects.filter(email=user)
    context={
        'orders': orders,
    }
    return render(request, 'orders.html', context)