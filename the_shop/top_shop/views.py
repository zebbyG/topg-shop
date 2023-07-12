from django.shortcuts import render
from theorders.models import Order


def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'home-shop.html', {"order": order})
    else:
        return render(request, 'home-shop.html')


def about(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'about-shop.html', {"order": order})
    else:
        return render(request, 'about-shop.html')


def contacts(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'contacts.html', {"order": order})
    else:
        return render(request, 'contacts.html')


def team(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'team.html', {"order": order})
    else:
        return render(request, 'team.html')
