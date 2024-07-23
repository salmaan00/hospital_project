from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('manage-users/', views.manage_users, name='manage_users'),
    path('manage-facility/', views.manage_facility, name='manage_facility'),
    path('manage-appointments/', views.manage_appointments, name='manage_appointments'),
    path('dashboard/', views.dashboard, name='admin-dashboard'),
    path('user-selection/', views.user_selection, name='user_selection'),
    path('manage_patients/', views.manage_patients, name='managepatients'),
    path('manage_doctors/', views.manage_doctors, name='manage_doctors'),
    path('edit_patient/<int:pk>/', views.edit_patient, name='edit_patient'),
    path('delete_patient/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('edit_doctor/<int:pk>/', views.edit_doctor, name='edit_doctor'),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('create-education-resources/', views.create_education_resources, name='create_education_resources'),
    path('admin-login/', AdminLoginView.as_view(), name='admin_login'),
    path('admin-dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('facility-list/', views.FacilityListView.as_view(), name='facility_list'),
    path('logou/', DoctorLogoutView.as_view(), name='adm_log'),
    path('manage-facilities/', views.manage_facilities, name='manage_facilities'),
    path('create-doctor/', create_doctor, name='create_doctor'),
]
