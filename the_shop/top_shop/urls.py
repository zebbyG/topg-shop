from django.urls import path
from . import views

app_name = 'introPage'

urlpatterns = [
    path('', views.home, name="home-page"),
    path('about/', views.about, name="about-page"),
    path('contacts/', views.contacts, name="contacts-page"),
    path('team/', views.team, name="team-page"),
]
