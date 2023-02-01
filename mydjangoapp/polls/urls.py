from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='indexy'),
   
    path('hello/<str:name>/<int:age>/',views.hello,name="hello"),
     path('<str:name>/',views.greet,name="greet"),
]
