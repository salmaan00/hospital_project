from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    medical_history = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    # additional fields as needed

    def username(self):
        return self.user.username

    def email(self):
        return self.user.email

class Appointment(models.Model):
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE, related_name='patient_appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointments')
    date = models.DateTimeField()
    # additional fields as needed

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    # additional fields as needed

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=(('Paid', 'Paid'), ('Unpaid', 'Unpaid')))
    # additional fields as needed

class HealthEducationResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='education_resources')

    # additional fields as needed