from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.patient_register, name='patient_register'),
    path('login/', views.patient_login, name='patient_login'),
    path('patient_profile/', views.patient_profile, name='patient_profile'),
    path('edit_profile/', views.edit_patient_profile, name='edit_patient_profile'),
    path('delete_profile/', views.delete_patient_profile, name='delete_patient_profile'),
    path('accounts/logout/', views.logout_view, name='logouts'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('medical-history/<int:patient_id>/', views.view_medical_history, name='view_medical_history'),
    path('billing/<int:patient_id>/', views.view_billing, name='view_billing'),
    path('health-education-resources/', views.health_education_resources, name='health_education_resources'),

]
