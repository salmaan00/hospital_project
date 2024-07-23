# doctor/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Doctor
from admin_app.models import UserManagement

User = get_user_model()

@receiver(post_save, sender=User)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created:
        try:
            user_management = instance.usermanagement
            if user_management.role == 'Doctor':
                Doctor.objects.create(user=instance)
        except UserManagement.DoesNotExist:
            pass

@receiver(post_save, sender=User)
def save_doctor_profile(sender, instance, **kwargs):
    try:
        instance.doctor.save()
    except Doctor.DoesNotExist:
        pass
