from django.shortcuts import render
from .models import Brands, Jordan


def catalogue(request):
    shop_brands = Brands.objects.all().order_by('time')
    return render(request, 'catalogue.html', {"shop_brands": shop_brands})


def jordans(request):
    jordan_shoes = Jordan.objects.all().order_by('shoe_time_added')
    return render(request, 'jordans.html', {"jordan_shoes": jordan_shoes})


def nikes(request):
    return render(request, 'nikes.html', {"name": "Zebbylion Njau"})


def vans(request):
    return render(request, 'vans.html', {"name": "Zebbylion Njau"})


def yeezys(request):
    return render(request, 'yeezys.html', {"name": "Zebbylion Njau"})


def pradas(request):
    return render(request, 'pradas.html', {"name": "Zebbylion Njau"})
