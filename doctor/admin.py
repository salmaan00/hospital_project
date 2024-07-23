# doctor/admin.py
from django.contrib import admin
from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'specialization', 'is_available']

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email


admin.site.register(Doctor, DoctorAdmin)