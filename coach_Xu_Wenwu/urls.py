from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('inscription/', views.signup),
    path('connexion/', views.signin),
    path('dashboard/', views.dashboard),
    path('rendez-vous/', views.appointment),
]