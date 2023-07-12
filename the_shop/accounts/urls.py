from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('sign_up/', views.sign_up, name="sign_up"),
    path('log_in/', views.log_in, name="log_in"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('profile_details/', views.profile_details, name="profile_details"),
    path('password_change/', views.password_change, name='password_change'),
    path('delete_profile_picture/', views.delete_profile_picture, name="delete_profile_picture"),
    path('log_out/', views.log_out, name="log_out")
]
