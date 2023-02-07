from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=64)
    city=models.CharField(max_length=64)
    def __str__(self):
        return f' code : {self.code} , city :{self.city}'
class flight(models.Model):
  origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departures')
  destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='arrivals')
  duration=models.IntegerField(default=0)
  date_de_depart=models.DateTimeField(blank=True ,null=True,default=datetime.datetime.now())
  def __str__(self):
    return f' flight from origin {self.origin} to destination : {self.destination}'
