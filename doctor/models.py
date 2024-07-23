from django.db import models
from patient.models import Patient, Appointment
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)
    # additional fields as needed

    def username(self):
        return self.user.username

    def email(self):
        return self.user.email

class PatientManagement(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_plan = models.TextField()
    # additional fields as needed

class AppointmentSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    # additional fields as needed

class EPrescribing(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.TextField()
    prescription_date = models.DateTimeField()
    # additional fields as needed

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"Dr. {self.username}"
