from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:log_in')
def add_to_cart(request):
    return render(request, 'add_to_cart.html')


def check_out(request):
    return render(request, 'check_out.html')
