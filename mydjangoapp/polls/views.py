from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
def greet(request,name):
    return HttpResponse(f"Hello your name is : {name}")
def hello(request,name,age):
    return render(request,"polls/index.html",{'name':name,'age':age})