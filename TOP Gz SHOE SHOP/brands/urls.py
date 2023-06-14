from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    path('Jordans/', views.jordans, name="Jordans"),
    path('Nikes/', views.nikes, name="Nikes"),
    path('Vans/', views.vans, name="Vans"),
    path('Yeezys/', views.yeezys, name="Yeezys"),
    path('Pradas/', views.pradas, name="Pradas"),
    path('shoes_accessories/', views.shoes_accessories, name="shoes_accessories"),
    path('', views.catalogue, name="catalogue"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('checkout/', views.check_out, name="checkout")
]

