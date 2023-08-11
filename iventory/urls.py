<<<<<<< HEAD
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("",TemplateView.as_view(template_name="iventory/index.html"))
=======
from django.contrib import admin
from django.urls import path ,include
from .views import Indexs
urlpatterns = [
 
     path('', Index.as_view(),name="index"),
>>>>>>> test
]
