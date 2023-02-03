from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from .models import PatientAdmission
from .serializers import PatientAdmissionSerializer

class PatientAdmissionViewSet(viewsets.ModelViewSet):

    serializer_class = PatientAdmissionSerializer
    permission_classes = ()
    queryset = PatientAdmission.objects.all()

    def get_queryset(self):
        patient_account = self.request.user.id
        queryset = self.queryset.filter(patient_account=patient_account)
        return queryset

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class PatientAccountViewSet(viewsets.ModelViewSet):

    serializer_class = PatientAdmissionSerializer
    queryset = PatientAdmission.objects.all()
    permission_classes = ()
    # authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get_queryset(self, *args, **kwargs):
        patient_account = self.request.user.id
        queryset = self.queryset.filter(patient_account=patient_account)
        print(f'Print:{patient_account}')
        return queryset

    def perform_update(self, serializer):
        return super().perform_update(serializer)





