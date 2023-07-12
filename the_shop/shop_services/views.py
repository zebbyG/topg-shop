from django.shortcuts import render
from theorders.models import Order


def services(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'shop-services.html', {"order": order})
    return render(request, 'shop-services.html')


def order_shoes(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'order-shoes.html', {"order": order})
    return render(request, 'order-shoes.html')


def trade(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'trade.html', {"order": order})
    return render(request, 'trade.html')


def customize_shoes(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'customize_shoes.html', {"order": order})
    return render(request, 'customize_shoes.html')


def donate_shoes(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'donate_shoes.html', {"order": order})
    return render(request, 'donate_shoes.html')


def customer_service(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'customer_service.html', {"order": order})
    return render(request, 'customer_service.html')

