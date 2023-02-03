from djoser.serializers import UserCreateSerializer

from rest_framework import serializers

from .models import Account

class AccountCreateSerializer(UserCreateSerializer):
    class Meta:
        model = Account
        fields = (
            'email',
            'last_name',
            'first_name',
            'middle_name',
            'sex',
            'birthdate',
            'home_no',
            'street',
            'address',
            'contact_number',
            # 'roles',
            'password',
            're_password'
        )




