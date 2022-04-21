from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError


class SalesStaff(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, 
            on_delete=models.CASCADE,)
    phone = models.CharField(max_length=255)

    def clean(self, *args, **kwargs):
        if GestionStaff.objects.filter(user=self.user).exists() or SupportStaff.objects.filter(user=self.user).exists():
            raise ValidationError("This user has already a role")
        self.user.is_staff = False
        self.user.save()
        super(SalesStaff, self).save(*args, **kwargs)


    def __str__(self):
        return self.full_name

class GestionStaff(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)

    def clean(self, *args, **kwargs):
        if SalesStaff.objects.filter(user=self.user).exists() or SupportStaff.objects.filter(user=self.user).exists():
            raise ValidationError("This user has already a role")
        self.user.is_staff = True
        self.user.save()
        super(GestionStaff, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class SupportStaff(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)

    def clean(self, *args, **kwargs):
        if SalesStaff.objects.filter(user=self.user).exists() or GestionStaff.objects.filter(user=self.user).exists():
            raise ValidationError("This user has already a role")
        self.user.is_staff = False
        self.user.save()
        super(SupportStaff, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class Client(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_staff = models.ForeignKey(to=SalesStaff, on_delete=models.CASCADE)
    converted = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Contract(models.Model):

    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    amount = models.FloatField(max_length=255)
    payment_due = models.DateTimeField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_staff = models.ForeignKey(to=SalesStaff, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

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
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True)
    support_staff = models.ForeignKey(to=SupportStaff, on_delete=models.CASCADE)
    event_status = models.ForeignKey(to=EventStatus, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name




