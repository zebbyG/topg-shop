from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='accounts:log_in')
def add_to_cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    items = order.orderitem_set.all()
    return render(request, 'add_to_cart.html', {"items": items, "order": order})


@login_required(login_url='accounts:log_in')
def check_out(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    items = order.orderitem_set.all()
    return render(request, 'check_out.html', {"items": items, "order": order})
