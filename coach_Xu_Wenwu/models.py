from django.db import models

class Users(models.Model):
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(max_length=100)
    email = models.fields.EmailField(max_length=300)
    password = models.fields.CharField(max_length=150)