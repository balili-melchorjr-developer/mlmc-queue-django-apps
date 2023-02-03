from rest_framework import serializers

from .models import PatientAdmission

class PatientAdmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientAdmission
        fields = (
            'id',
            'patient',
            'patient_account',
            'room',
            'admission_date',
            'nurse_call',
            'admitted_by',
            'created_by',
            'created_at',
            'modified_by',
            'modified_at',
        )

        # def get_queryset(self):
        #     user = self.context['request'].user
        #     qs = PatientAdmission.objects.filter(patient_account=6)           
        #     return qs

        # fields = ['__all__']

        depth = 2



