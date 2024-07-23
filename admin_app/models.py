from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class UserManagement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=(('Patient', 'Patient'), ('Doctor', 'Doctor'), ('Admin', 'Admin')))
    # additional fields as needed

class Facility(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    resources = models.TextField()
    # additional fields as needed

User = get_user_model()

class Appointment(models.Model):
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE, related_name='admin_appointments')
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE, related_name='admin_appointments')
    date = models.DateTimeField()
    # additional fields as needed

class AppointmentManagement(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=(('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')))
    # additional fields as needed

class Admin(models.Model):
    admin_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.admin_name
