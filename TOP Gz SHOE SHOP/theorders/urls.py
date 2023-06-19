from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('checkout/', views.check_out, name="checkout"),
]
