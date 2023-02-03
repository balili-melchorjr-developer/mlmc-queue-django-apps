from django.db import models

from account.models import Account
from room.models import RoomBuilder

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class Patient(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=200, choices=GENDER, default="Male")
    created_by = models.ForeignKey(Account, related_name='patient_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Account, related_name='patient_modified_by', on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"

class PatientAdmission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patient_account = models.ForeignKey(Account, related_name='patient_admission_patient_account', on_delete=models.CASCADE)
    room = models.ForeignKey(RoomBuilder, on_delete=models.CASCADE)
    admission_date = models.DateTimeField(auto_now_add=True)
    nurse_call = models.BooleanField(default=False)
    admitted_by = models.ForeignKey(Account, related_name='patient_admission_admitted_by', on_delete=models.CASCADE)
    created_by = models.ForeignKey(Account, related_name='patient_admission_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Account, related_name='patient_admission_modified_by', on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.last_name}, {self.patient.first_name} {self.patient.middle_name}"

