from django.shortcuts import render


def services(request):
    return render(request, 'services-shop.html', {"name": "Zebbylion Njau"})


def order_shoes(request):
    return render(request, 'order-shoes.html', {"name": "Zebbylion Njau"})


def trade(request):
    return render(request, 'trade.html', {"name": "Zebbylion Njau"})


def customize_shoes(request):
    return render(request, 'customize_shoes.html', {"name": "Zebbylion Njau"})


def shoes_accessories(request):
    return render(request, 'shoes_accessories.html', {"name": "Zebbylion Njau"})


def donate_shoes(request):
    return render(request, 'donate_shoes.html', {"name": "Zebbylion Njau"})
