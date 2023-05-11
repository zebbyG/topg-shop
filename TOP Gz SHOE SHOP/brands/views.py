from django.shortcuts import render


def catalogue(request):
    return render(request, 'catalogue.html', {"name": "Zebbylion njau"})


def jordans(request):
    return render(request, 'jordans.html', {"name": "Zebbylion Njau"})


def nikes(request):
    return render(request, 'nikes.html', {"name": "Zebbylion Njau"})


def vans(request):
    return render(request, 'vans.html', {"name": "Zebbylion Njau"})


def yeezys(request):
    return render(request, 'yeezys.html', {"name": "Zebbylion Njau"})


def pradas(request):
    return render(request, 'pradas.html', {"name": "Zebbylion Njau"})
