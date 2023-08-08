import time

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .models import *
from brands.models import Product, Size
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .forms import CommentForm


@login_required(login_url='accounts:log_in')
def add_to_cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    items = order.orderitem_set.all()
    size = Size.objects.all().order_by('-time_added')
    return render(request, 'add_to_cart.html', {
        "items": items,
        "order": order,
        "size": size
    })


@login_required(login_url='accounts:log_in')
def check_out(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    items = order.orderitem_set.all()
    shipping_address = ShippingAddress.objects.filter(user=customer).order_by('-date_added').first()
    return render(request, 'check_out.html', {
        "items": items,
        "order": order,
        "shipping_address": shipping_address,
    })


@login_required(login_url='accounts:log_in')
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


@login_required(login_url='accounts:log_in')
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
    template = render_to_string('order_email.html', {
        'name': request.user.username,
        'order_id': order.transaction_id,
        'items': order.orderitem_set.all,
        'total': order.get_cart_total,
        'total_products': order.get_cart_items,
    })

    email = EmailMessage(
        f'Your TOP Gz Order has been confirmed',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email]
    )
    email.fail_silently = False
    email.send()
    return JsonResponse('Payment completed successfully', safe=False)


@login_required(login_url='accounts:log_in')
def complete_orders(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    orders_completed = Order.objects.filter(user=customer, complete=True).order_by('-date_ordered')
    shipping_addresses = ShippingAddress.objects.filter(order__in=orders_completed)

    return render(request, 'complete_orders.html', {
        "orders_completed": orders_completed,
        "order": order,
        "shipping_addresses": shipping_addresses,
    })


@login_required(login_url='accounts:log_in')
def order_complete(request):
    customer = request.user
    order, completed = Order.objects.get_or_create(user=customer, complete=False)
    return render(request, 'order_completed.html', {
        "order": order
    })


@login_required(login_url='accounts:log_in')
def leave_comment(request):
    customer = request.user
    order, completed = Order.objects.get_or_create(user=customer, complete=False)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            template = render_to_string('comment_approval.html', {
                "comment": comment.comment,
                "name": request.user.username
            })
            email = EmailMessage(
                'Your comment has been received and is awaiting for approval',
                template,
                settings.EMAIL_HOST_USER,
                [request.user.email]
            )
            email.fail_silently = False
            email.send()
            time.sleep(2.5)
            return redirect('introPage:home-page')
    else:
        form = CommentForm()

    return render(request, 'comment.html', {"form": form, "order": order})
# def delete_order(request):
#     if request.method == 'POST':
#         order_id = request.POST.get('order_id')
#         order = Order.objects.get(id=order_id)
#         order.delete()
#         return JsonResponse({'message': 'Order deleted successfully.'})
#     return
