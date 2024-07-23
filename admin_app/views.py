from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import UserManagement, AppointmentManagement, Facility
from .forms import FacilityForm, EducationResourceForm, DoctorForm, PatientForm
from django.views.generic import ListView, TemplateView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from patient.models import Patient
from doctor.models import Doctor
from django.contrib.auth.decorators import login_required


def manage_users(request):
    users = UserManagement.objects.all()
    return render(request, 'admin/manage_users.html', {'users': users})

def manage_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request, 'admin/manage_facility.html', {'form': form})

def manage_appointments(request):
    appointments = AppointmentManagement.objects.all()
    return render(request, 'admin/manage_appointments.html', {'appointments': appointments})

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def user_selection(request):
    return render(request, 'selection.html')

@login_required
def manage_patients(request):
    user = request.user
    if hasattr(user, 'doctor'):
        doctor = user.doctor
        patients = doctor.patients.all()  # Assuming a reverse relation from Doctor to Patient
        return render(request, 'admin/manage_patients.html', {'patients': patients})
    else:
        # Handle the case where the doctor profile does not exist
        return render(request, 'admin/error.html', {'message': 'Doctor profile does not exist.'})

def manage_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'admin/manage_doctors.html', {'doctors': doctors})

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('manage_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'admin/edit_patient.html', {'form': form})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('manage_patients')

def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('manage_doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'admin/edit_doctor.html', {'form': form})

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect('manage_doctors')

def create_education_resources(request):
    if request.method == 'POST':
        # Handle form submission logic here
        pass
    return render(request, 'admins/create_education_resources.html')

class FacilityListView(ListView):
    model = Facility
    template_name = 'admin/facility_list.html'
    context_object_name = 'facilities'

def manage_facilities(request):
    return render(request, 'admin/manage_facilities.html')

class AdminLoginView(FormView):
    template_name = 'admin/admin_login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser:
            login(self.request, user)
            return redirect('admin_dashboard')  # Redirect to the admin dashboard
        return self.form_invalid(form)

class AdminDashboardView(TemplateView):
    template_name = 'admin/admin_dashboard.html'

class DoctorLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

def create_doctor(request):
    # Your logic to handle creating a doctor
    return render(request, 'admin/create_doctor.html')


def manage_appointments(request):
    appointments = AppointmentManagement.objects.all()
    return render(request, 'admin/manage_appointments.html', {'appointments': appointments})
