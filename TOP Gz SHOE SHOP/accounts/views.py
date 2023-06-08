from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from .models import UserProfile


def sign_up(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST, request.FILES)
        if sign_up_form.is_valid():
            user = sign_up_form.save()
            profile_picture = sign_up_form.cleaned_data['profile_pic']
            UserProfile.objects.create(user=user, profile_picture=profile_picture)
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
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if edit_profile_form.is_valid():
            user_profile = edit_profile_form.save(commit=False)  # Don't save yet

            # Check if a new profile picture is provided
            if 'profile_pic_change' in request.FILES:
                profile_picture = edit_profile_form.cleaned_data['profile_pic_change']
                user_profile = UserProfile.objects.get(user=request.user)
                user_profile.profile_picture = profile_picture
                user_profile.save()

            user_profile.save()
            return redirect('accounts:profile_details')
    else:
        edit_profile_form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'edit_profile_form': edit_profile_form})


def password_change(request):
    if request.method == 'POST':
        edit_password_form = ChangePasswordForm(request.user, request.POST)
        if edit_password_form.is_valid():
            edit_password_form.save()
            return redirect('accounts:log_in')
    else:
        edit_password_form = ChangePasswordForm(request.user)
    return render(request, 'change_password.html', {"edit_password_form": edit_password_form})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:log_in')
    return


def profile_details(request):
    return render(request, 'profile_details.html')
