from django.shortcuts import render


def home(request):
    return render(request, 'home-shop.html', {"name": "Zebbylion Njau"})


def catalogue(request):
    return render(request, 'accessories.html', {"name": "Zebbylion Njau"})


def about(request):
    return render(request, 'about-shop.html', {"name": "Zebbylion Njau"})


def contacts(request):
    return render(request, 'contacts.html', {"name": "Zebbylion Njau"})


def team(request):
    return render(request, 'team.html', {"name": "Zebbylion Njau"})
