from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .models import *
from brands.models import Product


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


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print("ProductId:", productId)
    print("Action:", action)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity < 1:
        orderItem.delete()

    return JsonResponse('item added successfully', safe=False)


def process_order(request):
    data = json.loads(request.body)
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    total = float(data['form']['total'])

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        user=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zip_code=data['shipping']['zipcode'],
        country=data['shipping']['country']
    )
    return JsonResponse('Payment completed successfully', safe=False)


# def complete_orders(request):
#     complete_order = (Order.transaction_id if Order.complete else "You have no completed orders")
#     customer = request.user
#     order, created = Order.objects.get_or_create(user=customer, complete=False)
#     return render(request, 'complete_orders.html', {"order": order, "complete_order": complete_order})
