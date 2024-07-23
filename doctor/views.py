from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View
from .forms import DoctorRegistrationForm,DoctorLoginForm
from django.shortcuts import render, redirect
from .models import Doctor, PatientManagement, AppointmentSchedule, EPrescribing
from .forms import DoctorProfileForm, PatientManagementForm, AppointmentScheduleForm, EPrescribingForm

def manage_patients(request):
    patients = PatientManagement.objects.filter(doctor=request.user.doctor)
    return render(request, 'doctor/manage_patients.html', {'patients': patients})

def view_appointments(request):
    appointments = AppointmentSchedule.objects.filter(doctor=request.user.doctor)
    return render(request, 'doctor/view_appointments.html', {'appointments': appointments})

def prescribe_medication(request):
    if request.method == 'POST':
        form = EPrescribingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = EPrescribingForm()
    return render(request, 'doctor/prescribe_medication.html', {'form': form})

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('doctor_dashboard')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor/register.html', {'form': form})

def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('doctor_dashboard')
    else:
        form = DoctorLoginForm()
    return render(request, 'doctor/login.html', {'form': form})

class DoctorLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor/doctor_dashboard.html')

@login_required
def doctor_profile(request):
    # Retrieve the Doctor profile using the User model
    profile = get_object_or_404(Doctor, user=request.user)
    return render(request, 'doctor/doctor_profile.html', {'profile': profile})


def my_view(request):
    # Example logic for the view
    return render(request, 'base.html')

@login_required
def view_doctor_profile(request):
    profile = get_object_or_404(Doctor, user=request.user)
    return render(request, 'doctor/view_profile.html', {'profile': profile})

@login_required
def edit_doctor_profile(request):
    profile = get_object_or_404(Doctor, user=request.user)
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('doctor_profile')  # Redirect to 'doctor_profile'
    else:
        form = DoctorProfileForm(instance=profile)
    return render(request, 'doctor/edit_profile.html', {'form': form})

@login_required
def delete_doctor_profile(request):
    profile = get_object_or_404(Doctor, user=request.user)
    if request.method == 'POST':
        profile.delete()
        return redirect('doctor_login')  # or any other redirect
    return render(request, 'doctor/delete_profile.html', {'profile': profile})



def about(request):
    return render(request, 'about.html')

def doctors(request):
    # Assuming you have a Doctor model
    doctors_list = Doctor.objects.all()
    context = {'doctors': doctors_list}
    return render(request, 'doctor.html', context)


def contact(request):
    return render(request, 'contact.html')

def news(request):
    # Assuming you have a News model
    news_list = Doctor.objects.all()
    context = {'news': news_list}
    return render(request, 'news.html', context)