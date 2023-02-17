from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.signup, name='signup'),
    path('sign-in/', views.signin, name='signin'),
    path('sign-out/', views.signout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appointment/', views.book_appointment, name='book_appointment'),
    path('history-appointment/', views.view_appointments, name='view_appointments'),
    path('history-appointment/<str:patient_name>/', views.patient_appointments, name="patient_appointments"),
    path('edit-notes/<int:appointment_id>/', views.edit_notes, name='edit_notes'),
    path('clients-list/', views.general_appointments_view, name='general_appointments_view')
]