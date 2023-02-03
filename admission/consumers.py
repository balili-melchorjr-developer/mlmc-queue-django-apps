import json

from asgiref.sync import sync_to_async

from .models import PatientAdmission
from account.models import Account

from .serializers import PatientAdmissionSerializer

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
from djangochannelsrestframework.mixins import ListModelMixin, RetrieveModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions
from djangochannelsrestframework.decorators import action

class PatientAdmissionDetailConsumer(ListModelMixin, GenericAsyncAPIConsumer):

    queryset = PatientAdmission.objects.all()
    serializer_class = PatientAdmissionSerializer
    permissions = (permissions.AllowAny, )

    async def connect(self, **kwargs):       
        
        # token = self.scope['query_string'].decode('utf-8')
        # try:
        #     token = Token.objects.get(key=token)
        #     self.user = Account.objects.get(id=token.user.id)
        # except Token.DoesNotExist:
        #     self.user = None
        # print(f'{username.last_name} {username} ID: {username.id}') 

        await self.model_change.subscribe()
        await super().connect()
        # await sync_to_async(print)(_variable_) '''This is how you print in consumbers'''

    @model_observer(PatientAdmission)
    async def model_change(self, message, observer=None, **kwargs): # any def name make sure there is observer at the top and models included
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        print(dict(data=PatientAdmissionSerializer(instance=instance).data, action=action.value))
        return dict(data=PatientAdmissionSerializer(instance=instance).data, action=action.value)

    def filter_queryset(self, queryset: PatientAdmission, **kwargs) -> PatientAdmission:
        username= self.scope['url_route']['kwargs']['account_number']
        qs = PatientAdmission.objects.filter(patient_account=username)
        return super().filter_queryset(qs, **kwargs)

    # @model_change.groups_for_signal
    # def patient_activity(self, instance: PatientAdmission, **kwargs):
    #     user = f'patient__account: {instance.patient_account.id}'
    #     yield(user)

    # @patient_admission_activity.serializer
    # def patient_admission_activity(self, instance: PatientAdmission, action, **kwargs) -> PatientAdmissionSerializer:
    #     '''This will return the patient admission serializer'''
    #     return PatientAdmissionSerializer(instance)

    # @patient_admission_activity.groups_for_signal
    # def patient_admission_activity(self, instance: PatientAdmission, **kwargs):
    #     # this block of code is called very often *DO NOT make DB QUERIES HERE*
    #     yield f'-user__{instance.patient_account_id}' #! the string **user** is sthe ``Patient Admission`` user field.

    # # @patient_admission_activity.groups_for_consumer
    # # def patient_admission_activity(self, school=None, classroom=None, **kwargs):
    # #     # This is call when you subscribe/unsubscribe
    # #     yield f'-user__{self.scope["user"].id}'

    # @action()
    # async def subscribe_to_patient_admission_activity(self, request_id, **kwargs):
    #     # We will check if the user is authenticated for subscribing.
    #     if "user" in self.scope and self.scope["user"].is_authenticated:
    #         await self.patient_admission_activity.subscribe(request_id=request_id)

class PatientAdmissionConsumer(ListModelMixin, GenericAsyncAPIConsumer):

    queryset = PatientAdmission.objects.all()
    serializer_class = PatientAdmissionSerializer
    permissions = (permissions.AllowAny, )

    async def connect(self, **kwargs):          

        await self.model_change.subscribe()
        await super().connect()

    @model_observer(PatientAdmission)
    async def model_change(self, message, observer=None, **kwargs): # any def name make sure there is observer at the top and models included
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        return dict(data=PatientAdmissionSerializer(instance=instance).data, action=action.value)




