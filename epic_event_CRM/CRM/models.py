from django.db import models
from django.contrib.auth.models import User


class SalesStaff(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)

class GestionStaff(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)

class SupportStaff(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)

class Client(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Contract(models.Model):

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    payment_due = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):

    name = models.CharField(max_length=255)
    attendees = models.CharField(max_length=255)
    event_date = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
