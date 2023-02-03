from django.contrib import admin

from admission.models import Patient, PatientAdmission

admin.site.register(Patient)
admin.site.register(PatientAdmission)
