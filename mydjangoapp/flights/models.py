from django.db import models

# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=64)
    city=models.CharField(max_length=64)
class flight(models.Model):
  origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departures')
  destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='arrivals')
  duration=models.IntegerField(default=0)
