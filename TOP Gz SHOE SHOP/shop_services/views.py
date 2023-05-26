from django.shortcuts import render


def services(request):
    return render(request, 'shop-services.html', {"name": "Zebbylion Njau"})


def order_shoes(request):
    return render(request, 'order-shoes.html', {"name": "Zebbylion Njau"})


def trade(request):
    return render(request, 'trade.html', {"name": "Zebbylion Njau"})


def customize_shoes(request):
    return render(request, 'customize_shoes.html', {"name": "Zebbylion Njau"})


def donate_shoes(request):
    return render(request, 'donate_shoes.html', {"name": "Zebbylion Njau"})


def customer_service(request):
    return render(request, 'customer_service.html', {"name": "Zebbylion njau"})

