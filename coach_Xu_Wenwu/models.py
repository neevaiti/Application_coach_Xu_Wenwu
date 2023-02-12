from django.contrib.auth.models import User
from django.db import models

class PickDate(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    time_slot = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)