from django.shortcuts import render
from django.http import HttpResponse
from .models import flight
# Create your views here.
def index(request):
  return render(request,"flights/index.html",{
    'Flights' : flight.objects.all()
  })