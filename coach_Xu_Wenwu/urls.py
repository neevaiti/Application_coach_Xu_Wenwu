from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('inscription/', views.signup),
    path('connexion/', views.signin),
    path('signout/', views.signout),
    path('dashboard/', views.dashboard),
    path('rendez-vous/', views.book_appointment),
    path('historique-rendez-vous/', views.view_appointments),
    path('historique-rendez-vous/<str:patient_name>/', views.patient_appointments, name='patient_appointments'),
    path('edit_notes/<int:appointment_id>/', views.edit_notes, name='edit_notes'),
    path('liste-patients/', views.general_appointments_view)
]