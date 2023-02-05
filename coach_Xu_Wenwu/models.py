from django.db import models

class Users(models.Model):
    name = models.fields.CharField(max_length=100, null=False, blank=False)
    surname = models.fields.CharField(max_length=100, null=False, blank=False)
    phone = models.fields.IntegerField(null=False, blank=False)
    email = models.fields.EmailField(max_length=300, null=False, blank=False)
    password = models.fields.CharField(max_length=150, null=False, blank=False)