from django.db import models
from django.contrib.auth.models import User


class SalesStaff(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class GestionStaff(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class SupportStaff(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class Client(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_staff = models.ForeignKey(to=SalesStaff, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name


class Contract(models.Model):

    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    amount = models.FloatField(max_length=255)
    payment_due = models.DateTimeField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_staff = models.ForeignKey(to=SalesStaff, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class EventStatus(models.Model):

    active = models.BooleanField(default=True)

    def __str__(self):
        if self.active == True:
            return "status : active"
        return "status : inactive"


class Event(models.Model):

    name = models.CharField(max_length=255)
    attendees = models.CharField(max_length=255)
    event_date = models.CharField(max_length=255)
    notes = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_staff = models.ForeignKey(to=SupportStaff, on_delete=models.CASCADE, null=True)
    event_status = models.ForeignKey(to=EventStatus, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name




