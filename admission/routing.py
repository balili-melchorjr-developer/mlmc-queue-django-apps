from django.urls import re_path

from djangochannelsrestframework.consumers import view_as_consumer

from .views import PatientAccountViewSet

from .consumers import (
    PatientAdmissionDetailConsumer,
    PatientAdmissionConsumer
)
    

websocket_urlpatterns = [
    # re_path(r'^ws/patient-admission/$', PatientAdmissionConsumer.as_asgi()),
    re_path(r'^ws/patient-admission/$', PatientAdmissionConsumer.as_asgi()),
    re_path(r'^ws/patient-account/(?P<account_number>\w+)/$', PatientAdmissionDetailConsumer.as_asgi()),
    # re_path(r'^ws/patient-account/$', view_as_consumer(PatientAccountViewSet.as_view({'get': 'list'}))),  
#    re_path(r'^ws/patient-account/(?P<account_number>\w+)/$', consumers.MyConsumer.as_asgi()), 
]