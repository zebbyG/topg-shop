from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def sign_up(request):
    if request.method == 'POST':
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            user = sign_up_form.save()
            login(request, user)
            return redirect('accounts:log_in')
    else:
        sign_up_form = UserCreationForm()
    return render(request, 'sign-up.html', {"sign_up_form": sign_up_form})


def log_in(request):
    if request.method == 'POST':
        log_in_form = AuthenticationForm(data=request.POST)
        if log_in_form.is_valid():
            user = log_in_form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('introPage:home-page')
    else:
        log_in_form = AuthenticationForm()
    return render(request, 'log_in.html', {"log_in_form": log_in_form})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('introPage:home-page')
    return
