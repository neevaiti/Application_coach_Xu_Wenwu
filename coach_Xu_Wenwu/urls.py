from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('accueil/', views.home),
    path('inscription/', views.signup),
    path('connexion/', views.signin),
    path('deconnexion/', views.logout),
]