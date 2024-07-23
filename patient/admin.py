from django.contrib import admin
from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'date_of_birth', 'gender']

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email


admin.site.register(Patient, PatientAdmin)