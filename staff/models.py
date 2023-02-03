from django.db import models
from django.contrib.auth.models import User

from room.models import NurseStationBuilder
from account.models import Account

class ScheduleBuilder(models.Model):
    created_by = models.ForeignKey(Account, related_name='schedule_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Account, related_name='schedule_modified_by', on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "hello"

class StaffNurse(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    schedule = models.ForeignKey(ScheduleBuilder, on_delete=models.CASCADE)
    nurse_station = models.ForeignKey(NurseStationBuilder, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Account, related_name='staff_nurse_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Account, related_name='staff_nurse_modified_by', on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.nurse_station}"
    

