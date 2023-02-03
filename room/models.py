from django.contrib.auth.models import User
from django.db import models

from account.models import Account

NURSE_STATION_STATUS = (
    ('Under Renovation', 'Under Renovation'),
    ('Available', 'Available'),
)

ROOM_STATUS = (
    ('Cleaning', 'Cleaning'),
    ('Available', 'Available'),
    ('Occupied', 'Occupied'),
    ('Under Renovation', 'Under Renovation'),
)

class NurseStationBuilder(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(default='Available', choices=NURSE_STATION_STATUS, max_length=200)
    created_by = models.ForeignKey(Account, related_name='nurse_station_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Account, related_name='nurse_station_modified_by', on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class RoomBuilder(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(default='Available', choices=ROOM_STATUS, max_length=200)
    nurse_station = models.ForeignKey(NurseStationBuilder, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Account, related_name='room_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Account, related_name='room_modified_by', on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    

