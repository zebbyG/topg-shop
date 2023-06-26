from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from .models import UserProfile

from django.core.files.storage import default_storage
from django.http import JsonResponse
from theorders.models import Order


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
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if edit_profile_form.is_valid():
            user_profile = edit_profile_form.save()

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
    return render(request, 'edit_profile.html', {'edit_profile_form': edit_profile_form, "order": order})


def password_change(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    if request.method == 'POST':
        edit_password_form = ChangePasswordForm(request.user, request.POST)
        if edit_password_form.is_valid():
            edit_password_form.save()
            return redirect('accounts:log_in')
    else:
        edit_password_form = ChangePasswordForm(request.user)
    return render(request, 'change_password.html', {"edit_password_form": edit_password_form, "order": order})


def profile_details(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    return render(request, 'profile_details.html', {"order": order})


def delete_profile_picture(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_profile = UserProfile.objects.get(user_id=user_id)

        # Delete the profile picture file from storage
        if user_profile.profile_picture:
            default_storage.delete(user_profile.profile_picture.path)

        # Set the profile picture field to None
        user_profile.profile_picture = None
        user_profile.save()

        return JsonResponse({'message': 'Profile picture deleted.'})
    return JsonResponse({'error': 'Invalid request method.'})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:log_in')
    return
