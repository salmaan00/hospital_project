from django.urls import path
from .views import*
from . import views

urlpatterns = [
    path('', my_view, name='my_view'),
    path('register/', doctor_register, name='doctor_register'),
    path('login/', doctor_login, name='doctor_login'),
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('profile/', views.doctor_profile, name='doctor_profile'),
    path('profile/edit/', views.edit_doctor_profile, name='edit_profile'),
    path('profile/delete/', views.delete_doctor_profile, name='delete_profile'),
    path('profile/view/', views.view_doctor_profile, name='view_profile'),
    path('logout/', DoctorLogoutView.as_view(), name='doctor_logout'),
    path('manage-patients/', views.manage_patients, name='manage_patients'),
    path('view-appointments/', views.view_appointments, name='view_appointments'),
    path('doct/', doctors, name='doctors'),
    path('prescribe-medication/', views.prescribe_medication, name='prescribe_medication'),
]
