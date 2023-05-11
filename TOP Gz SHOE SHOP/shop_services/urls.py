from django.urls import path
from . import views

app_name = 'servicesPage'

urlpatterns = [
    path('', views.services, name="services-page"),
    path('order-shoes/', views.order_shoes, name="order-shoes"),
    path('trade/', views.trade, name="trade"),
    path('customize_shoes/', views.customize_shoes, name="customize_shoes"),
    path('shoes_accessories/', views.shoes_accessories, name="shoes_accessories"),
    path('donate_shoes/', views.donate_shoes, name="donate_shoes"),
]
