from .models import Doctor
from django import forms
from .models import PatientManagement, AppointmentSchedule, EPrescribing
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientManagementForm(forms.ModelForm):
    class Meta:
        model = PatientManagement
        fields = '__all__'

class AppointmentScheduleForm(forms.ModelForm):
    class Meta:
        model = AppointmentSchedule
        fields = '__all__'

class EPrescribingForm(forms.ModelForm):
    class Meta:
        model = EPrescribing
        fields = '__all__'

class DoctorRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            doctor = Doctor(user=user, first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'])
            doctor.save()
        return user

class DoctorLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)