from django.contrib.auth import login, authenticate, logout
from .forms import PatientForm, AppointmentForm, PatientRegistrationForm, PatientLoginForm
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render, redirect
from .models import*
from .forms import PatientForm, AppointmentForm, BillingForm,PatientProfileForm
from doctor.models import Doctor
from django.contrib.auth.decorators import login_required

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_profile')
    else:
        form = PatientForm()
    return render(request, 'patient/register.html', {'form': form})

# views.py
@login_required
def book_appointment(request):
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'patient/book_appointment.html', {
        'form': form,
        'doctors': doctors
    })

@login_required
def view_medical_history(request, patient_id):
    medical_history = MedicalHistory.objects.filter(patient_id=patient_id)
    return render(request, 'patient/medical_history.html', {'medical_history': medical_history})

@login_required
def view_billing(request, patient_id):
    billing = Billing.objects.filter(patient_id=patient_id)
    return render(request, 'patient/billing.html', {'billing': billing})

@login_required
def health_education_resources(request):
    resources = HealthEducationResource.objects.all()
    return render(request, 'patient/health_education_resources.html', {'resources': resources})
# Authentication views

def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_login')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient/register.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient_profile')
    else:
        form = PatientLoginForm()
    return render(request, 'patient/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def patient_profile(request):
    patient = get_object_or_404(Patient, user=request.user)
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'patient/patient_profile.html', {
        'patient': patient,
        'doctors': doctors,
        'appointments': appointments,
    })

def edit_patient_profile(request):
    patient = get_object_or_404(Patient, user=request.user)
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_profile')
    else:
        form = PatientProfileForm(instance=patient)
    return render(request, 'patient/edit_profile.html', {'form': form})

@login_required
def delete_patient_profile(request):
    patient = get_object_or_404(Patient, user=request.user)
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()  # This will delete the user and the patient profile
        return redirect('/')  # Redirect to homepage or login page after deletion
    return render(request, 'patient/delete_profile.html')

# views.py

