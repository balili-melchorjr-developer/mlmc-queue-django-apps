from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator

from roles.models import RoleBuilder

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class MyAccountManager(BaseUserManager):
    def create_user(
        self,
        email,
        password=None,
        last_name=None,
        first_name=None,
        middle_name=None,
        sex=None,
        birthdate=None,
        home_no=None,
        street=None,
        address=None,
        contact_number=None,
        roles=None,        
    ):
        if not email:
            raise ValueError("User have must and email address")

        user = self.model(
            email=self.normalize_email(email),
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            sex=sex,
            birthdate=birthdate,
            home_no=home_no,
            street=street,
            address=address,
            contact_number=contact_number,
            roles=roles
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(email),
        password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self.db)
        return user   

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', unique=True, max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=200, choices=GENDER, default='Male', null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    home_no = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(null=True, blank=True, verbose_name='Contact Number', max_length=15, validators=[RegexValidator(r'^\d{0,15}$')])
    profile_pic = models.FileField(null=True, blank=True)
    roles = models.ForeignKey(RoleBuilder, on_delete=models.CASCADE, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date-joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last-login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'last_name',
        'first_name',
        'middle_name',
        'sex',
        'birthdate',
        'home_no',
        'street',
        'address',
        'contact_number',
        'roles'
    ]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"

    def has_perm(self, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True