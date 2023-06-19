from django.shortcuts import render
from .models import Brand, Product
from django.shortcuts import get_object_or_404


def catalogue(request):
    shop_brands = Brand.objects.all().order_by('-time')
    return render(request, 'catalogue.html', {"shop_brands": shop_brands})


def jordans(request):
    jordan_brand = get_object_or_404(Brand, brand_name='Jordans')
    jordan_shoes = Product.objects.filter(brand=jordan_brand).order_by('-shoe_time_added')
    return render(request, 'jordans.html', {"jordan_shoes": jordan_shoes})


def nikes(request):
    nike_brand = get_object_or_404(Brand, brand_name='Nikes')
    nike_shoes = Product.objects.filter(brand=nike_brand).order_by('-shoe_time_added')
    return render(request, 'nikes.html', {"nike_shoes": nike_shoes})


def vans(request):
    vans_brand = get_object_or_404(Brand, brand_name='Vans')
    vans_shoes = Product.objects.filter(brand=vans_brand).order_by('-shoe_time_added')
    return render(request, 'vans.html', {"vans_shoes": vans_shoes})


def yeezys(request):
    yeezy_brand = get_object_or_404(Brand, brand_name='Yeezys')
    yeezy_shoes = Product.objects.filter(brand=yeezy_brand).order_by('-shoe_time_added')
    return render(request, 'yeezys.html', {"yeezy_shoes": yeezy_shoes})


def pradas(request):
    prada_brand = get_object_or_404(Brand, brand_name='Pradas')
    prada_shoes = Product.objects.filter(brand=prada_brand).order_by('-shoe_time_added')
    return render(request, 'pradas.html', {"prada_shoes": prada_shoes})


def shoes_accessories(request):
    shoes_accessories_brand = get_object_or_404(Brand, brand_name='shoes_accessories')
    shoes_accessories_products = Product.objects.filter(brand=shoes_accessories_brand).order_by('-shoe_time_added')
    return render(request, 'shoes_accessories.html', {"shoes_accessories_products": shoes_accessories_products})
