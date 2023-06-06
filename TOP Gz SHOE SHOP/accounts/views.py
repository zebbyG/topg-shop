from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignUpForm, EditProfileForm, EditPasswordForm


def sign_up(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            user = sign_up_form.save()
            login(request, user)
            return redirect('accounts:log_in')
    else:
        sign_up_form = SignUpForm()
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


def edit_profile(request):
    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, instance=request.user)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return redirect('introPage:home-page')
    else:
        edit_profile_form = EditProfileForm(instance=request.user)
        return render(request, 'edit_profile.html', {'edit_profile_form': edit_profile_form})


def password_change(request):
    if request.method == 'POST':
        edit_password_form = EditPasswordForm(request.POST, instance=request.user)
        if edit_password_form.is_valid():
            edit_password_form.save()
            return redirect('accounts:edit_profile')
    else:
        edit_password_form = EditPasswordForm
        return render(request, 'change_password.html', {"edit_password_form": edit_password_form})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:log_in')
    return


def profile_details(request):
    return render(request, 'profile_details.html')
