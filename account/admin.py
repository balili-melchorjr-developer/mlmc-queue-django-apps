from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account

class AccountAdmin(UserAdmin):
    
    model = Account

    list_display = (
        'full_name',
        'email'
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('profile_pic', 'last_name', 'first_name', 'middle_name', 'sex', 'birthdate', 'home_no', 'street', 'address', 'contact_number',)}),
        ('Permissions', {'fields': ('roles', 'is_admin', 'is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('profile_pic', 'last_name', 'first_name', 'middle_name', 'sex', 'birthdate', 'home_no', 'street', 'address', 'contact_number',)}),
        ('Permissions', {'fields': ('roles', 'is_admin', 'is_active', 'is_staff', 'is_superuser')})
    )

    ordering = ('email',)
    exclude = ['date_joined', 'last_login']

admin.site.register(Account, AccountAdmin)
