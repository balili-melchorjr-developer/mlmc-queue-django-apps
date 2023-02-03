from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientAdmissionViewSet, PatientAccountViewSet

router = DefaultRouter()

router.register('patient-admission', PatientAdmissionViewSet, basename='patient-admission')
router.register('patient-account', PatientAccountViewSet, basename='patient-account')

urlpatterns = [
    path('', include(router.urls))
]



