from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    path('live/',views.live,name='live'),
    
    path('boardexams/',views.boardexams,name='boardexams'),
    path('schoolexams/',views.schoolexams,name='schoolexams'),
    path('jeemain/',views.jeemain,name='jeemain'),
    path('jeeadvance/',views.jeeadvance,name='jeeadvance'),
    path('neet/',views.neet,name='neet'),
    path('previousyear/',views.previousyear,name='previousyear'),
    
    path('book/',views.book,name='book'),
    path('book1/',views.book1,name='book1'),
    path('ncert/',views.ncert,name='ncert'),
    path('chapter1/',views.chapter1,name='chapter1'),
    path('exercise/',views.exercise,name='exercise'),
    path('question/',views.question,name='question'),
    
    path('course/',views.course,name='course'),
    path('join/',views.join,name='join'),
    
    path('board/',views.board,name='board'),
    
]