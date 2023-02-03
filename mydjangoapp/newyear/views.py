from django.shortcuts import render
import datetime
# Create your views here.
def newyear(request):
 x = datetime.datetime.now()

 return render(request,"newyear/index.html",{
'newyearday':x

 })