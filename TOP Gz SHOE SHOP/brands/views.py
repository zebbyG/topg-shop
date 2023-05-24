from django.shortcuts import render
from .models import Brand, Shoe
from django.shortcuts import get_object_or_404


def catalogue(request):
    shop_brands = Brand.objects.all()
    return render(request, 'catalogue.html', {"shop_brands": shop_brands})


def jordans(request):
    jordan_brand = get_object_or_404(Brand, brand_name='Jordans')
    jordan_shoes = Shoe.objects.filter(brand=jordan_brand).order_by('shoe_time_added')
    return render(request, 'jordans.html', {"jordan_shoes": jordan_shoes})


def nikes(request):
    nike_brand = get_object_or_404(Brand, brand_name='Nikes')
    nike_shoes = Shoe.objects.filter(brand=nike_brand).order_by('shoe_time_added')
    return render(request, 'nikes.html', {"nike_shoes": nike_shoes})


def vans(request):
    vans_brand = get_object_or_404(Brand, brand_name='Vans')
    vans_shoes = Shoe.objects.filter(brand=vans_brand).order_by('shoe_time_added')
    return render(request, 'vans.html', {"vans_shoes": vans_shoes})


def yeezys(request):
    yeezy_brand = get_object_or_404(Brand, brand_name='Yeezys')
    yeezy_shoes = Shoe.objects.filter(brand=yeezy_brand).order_by('shoe_time_added')
    return render(request, 'yeezys.html', {"yeezy_shoes": yeezy_shoes})


def pradas(request):
    prada_brand = get_object_or_404(Brand, brand_name='Pradas')
    prada_shoes = Shoe.objects.filter(brand=prada_brand).order_by('shoe_time_added')
    return render(request, 'pradas.html', {"prada_shoes": prada_shoes})
