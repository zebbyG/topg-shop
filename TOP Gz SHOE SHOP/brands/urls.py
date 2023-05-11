from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    path('jordans/', views.jordans, name="jordans"),
    path('nikes/', views.nikes, name="nikes"),
    path('vans/', views.vans, name="vans"),
    path('yeezys/', views.yeezys, name="yeezys"),
    path('pradas/', views.pradas, name="pradas"),
    path('catalogue/', views.catalogue, name="catalogue")
]
