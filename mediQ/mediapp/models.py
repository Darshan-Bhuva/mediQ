from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.db import models

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True, unique=True)
    specialization = models.CharField(max_length=100)
    fname = models.CharField(max_length=255)
    sname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=10)
    emergency_phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    dob = models.DateField()

    def save(self, *args, **kwargs):
        # Hash the password before saving the model
        self.password = make_password(self.password)
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return f"Doctor {self.doctor_id} for{self.fname} {self.sname}"


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField(max_length=254)
    fname = models.CharField(max_length=255)
    sname = models.CharField(max_length=255)
    disease = models.JSONField(max_length=100, default=list)
    time_duration = models.DurationField()
    symptoms = models.JSONField(max_length=100, default=list)
    causes_of_disease = models.JSONField(max_length=100, default=list)
    allergy = models.JSONField(max_length=100, default=list)
    date = models.DateField(default=timezone.now)
    slot_time = models.TimeField()
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    allocated_time = models.TimeField()
    allocated_date = models.DateField()

    def __str__(self):
        return f"Appointment {self.appointment_id} for {self.fname} {self.sname}"


class User(models.Model):
    fname = models.CharField(max_length=255)
    sname = models.CharField(max_length=255)
    email = models.EmailField(primary_key=True, unique=True)
    phone_no = models.CharField(max_length=10)
    emergency_phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    dob = models.DateField()

    def save(self, *args, **kwargs):
        # Hash the password before saving the model
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.fname} {self.sname}"
