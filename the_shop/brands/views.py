from django.shortcuts import render
from .models import Brand, Product, Size
from django.shortcuts import get_object_or_404
from theorders.models import Order


def catalogue(request):
    shop_brands = Brand.objects.all().order_by('-brand_in_stock', '-time')
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'catalogue.html', {"shop_brands": shop_brands, "order": order})
    return render(request, 'catalogue.html', {"shop_brands": shop_brands})


def jordans(request):
    jordan_brand = get_object_or_404(Brand, brand_name='Jordans')
    jordan_shoes = Product.objects.filter(brand=jordan_brand).order_by('-shoe_in_stock', '-shoe_time_added')
    # size = Size.objects.all().order_by('-time_added')
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'jordans.html', {
            "jordan_shoes": jordan_shoes,
            "order": order,
        })
    return render(request, 'jordans.html', {
        "jordan_shoes": jordan_shoes,
    })


def nikes(request):
    nike_brand = get_object_or_404(Brand, brand_name='Nikes')
    nike_shoes = Product.objects.filter(brand=nike_brand).order_by('-shoe_in_stock', '-shoe_time_added')
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'nikes.html', {"nike_shoes": nike_shoes, "order": order})
    return render(request, 'nikes.html', {"nike_shoes": nike_shoes})


def vans(request):
    vans_brand = get_object_or_404(Brand, brand_name='Vans')
    vans_shoes = Product.objects.filter(brand=vans_brand).order_by('-shoe_in_stock', '-shoe_time_added')
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'vans.html', {"vans_shoes": vans_shoes, "order": order})
    return render(request, 'vans.html', {"vans_shoes": vans_shoes})


def yeezys(request):
    yeezy_brand = get_object_or_404(Brand, brand_name='Yeezys')
    yeezy_shoes = Product.objects.filter(brand=yeezy_brand).order_by('-shoe_in_stock', '-shoe_time_added')
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'yeezys.html', {"yeezy_shoes": yeezy_shoes, "order": order})
    return render(request, 'yeezys.html', {"yeezy_shoes": yeezy_shoes})


def pradas(request):
    prada_brand = get_object_or_404(Brand, brand_name='Pradas')
    prada_shoes = Product.objects.filter(brand=prada_brand).order_by('-shoe_in_stock', '-shoe_time_added')
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'pradas.html', {"prada_shoes": prada_shoes, "order": order})
    return render(request, 'pradas.html', {"prada_shoes": prada_shoes})


def shoes_accessories(request):
    shoes_accessories_brand = get_object_or_404(Brand, brand_name='Shoes Accessories')
    shoes_accessories_products = Product.objects.filter(brand=shoes_accessories_brand).order_by('-shoe_in_stock', '-shoe_time_added')
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'shoes_accessories.html', {"shoes_accessories_products": shoes_accessories_products, "order": order})
    return render(request, 'shoes_accessories.html', {"shoes_accessories_products": shoes_accessories_products})


def pumas(request):
    puma_brand = get_object_or_404(Brand, brand_name='Pumas')
    puma_shoes = Product.objects.filter(brand=puma_brand).order_by('-shoe_in_stock', '-shoe_time_added')
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'pumas.html', {
            "puma_shoes": puma_shoes,
            "order": order
        })
    return render(request, 'pumas.html', {
        "puma_shoes": puma_shoes
    })


def balenciagas(request):
    balenciaga_brand = get_object_or_404(Brand, brand_name='Balenciagas')
    balenciaga_shoes = Product.objects.filter(brand=balenciaga_brand)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'balenciagas.html', {
            "balenciaga_shoes": balenciaga_shoes,
            "order": order
        })
    return render(request, 'balenciagas.html', {
        "balenciaga_shoes": balenciaga_shoes
    })


def gucci(request):
    gucci_brand = get_object_or_404(Brand, brand_name="Gucci")
    gucci_shoes = Product.objects.filter(brand=gucci_brand)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'gucci.html', {
            "gucci_shoes": gucci_shoes,
            "order": order
        })
    return render(request, 'gucci.html', {
        "gucci_shoes": gucci_shoes
    })


def louis_vuitton(request):
    louis_vuitton_brand = get_object_or_404(Brand, brand_name="Louis Vuitton")
    louis_vuitton_shoes = Product.objects.filter(brand=louis_vuitton_brand)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'louis_vuitton.html', {
            "louis_vuitton_shoes": louis_vuitton_shoes,
            "order": order
        })
    return render(request, 'louis_vuitton.html', {
        "louis_vuitton_shoes": louis_vuitton_shoes
    })


def versace(request):
    versace_brand = get_object_or_404(Brand, brand_name="Versace")
    versace_shoes = Product.objects.filter(brand=versace_brand)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'versace.html', {
            "versace_shoes": versace_shoes,
            "order": order
        })
    return render(request, 'versace.html', {
        "versace_shoes": versace_shoes
    })


def addidas(request):
    addidas_brand = get_object_or_404(Brand, brand_name="Addidas")
    addidas_shoes = Product.objects.filter(brand=addidas_brand)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'addidas.html', {
            "addidas_shoes": addidas_shoes,
            "order": order
        })
    return render(request, 'addidas.html', {
        "addidas_shoes": addidas_shoes
    })
