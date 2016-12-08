from django.db import models

import datetime
from django.utils import timezone
# Create your models here.
class Address(models.Model):
  ip_address = models.CharField(max_length=200)
  first_connect = models.DateTimeField('date first accessed on address')

  def created_recently(self):
    return self.first_connect >= timezone.now() - datetime.timedelta(days=1)
  
  def __str__(self):
    return self.ip_address

class Location(models.Model):
  address = models.ForeignKey(Address, on_delete=models.CASCADE)
  ip_version = models.IntegerField(default=4)
  country = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  region = models.CharField(max_length=100)
  postal_code = models.IntegerField(default=0)

  def __str__(self):
    return str([self.country, self.city, self.region])
