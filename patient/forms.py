from django import forms
from .models import Patient,Appointment,Billing
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientRegistrationForm(UserCreationForm):
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
            patient = Patient(user=user, first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'])
            patient.save()
        return user


class PatientLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields= '__all__'


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields= '__all__'