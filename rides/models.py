from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64, default='') # new
  origination = models.CharField(max_length=64)
  origination_state = models.CharField(max_length=2, default='') # new
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  pet_friendly = models.BooleanField(default=False)
  accessible = models.BooleanField(default=False)
  seats_available = models.IntegerField(default='')
  # Define your choices as a list of tuples
  VEHICLE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Minivan', 'Minivan'),
        ('Van', 'Van'),
        ('Truck', 'Truck'),
        ('Other', 'Other'),
  ]
  # Add the new field with the choices parameter
  vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES, default='Sedan') # new
