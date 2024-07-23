from django import forms
from .models import UserManagement, Facility, AppointmentManagement, Admin
from patient.models import Patient, HealthEducationResource
from doctor.models import Doctor

class UserManagementForm(forms.ModelForm):
    class Meta:
        model = UserManagement
        fields = '__all__'

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = '__all__'

class AppointmentManagementForm(forms.ModelForm):
    class Meta:
        model = AppointmentManagement
        fields = '__all__'

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['admin_name', 'email', 'password']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class EducationResourceForm(forms.ModelForm):
    class Meta:
        model = HealthEducationResource
        fields = '__all__'
