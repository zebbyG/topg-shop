from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    path('Jordans/', views.jordans, name="Jordans"),
    path('Nikes/', views.nikes, name="Nikes"),
    path('Vans/', views.vans, name="Vans"),
    path('Yeezys/', views.yeezys, name="Yeezys"),
    path('Pradas/', views.pradas, name="Pradas"),
    path('Shoes Accessories/', views.shoes_accessories, name="Shoes Accessories"),
    path('Pumas/', views.pumas, name="Pumas"),
    path('Balenciagas/', views.balenciagas, name="Balenciagas"),
    path('Gucci/', views.gucci, name="Gucci"),
    path('Louis Vuitton/', views.louis_vuitton, name="Louis Vuitton"),
    path('Versace/', views.versace, name="Versace"),
    path('Addidas/', views.addidas, name="Addidas"),
    path('', views.catalogue, name="catalogue"),
]
