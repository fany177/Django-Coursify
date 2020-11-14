from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('slide9/',views.slide9,name='slide9'),
    path('slide10/',views.slide10,name='slide10'),
    path('slide13/',views.slide13,name='slide13'),
    path('slide14/',views.slide14,name='slide14'),
    path('slide15/',views.slide15,name='slide15'),
    path('slide19/',views.slide19,name='slide19'),
    path('boardexams/',views.boardexams,name='boardexams'),
    path('schoolexams/',views.schoolexams,name='schoolexams'),
    path('jeemain/',views.jeemain,name='jeemain'),
]