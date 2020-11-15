from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('course/',views.course,name='course'),
    path('board',views.board,name='board'),
    path('book/',views.book,name='book'),
    path('book1/',views.book1,name='book1'),
    path('book2/',views.book2,name='book2'),
    path('book3/',views.book3,name='book3'),
    path('video/',views.video,name='video'),
    path('join/',views.join,name='join'),
    path('boardexams/',views.boardexams,name='boardexams'),
    path('schoolexams/',views.schoolexams,name='schoolexams'),
    path('jeemain/',views.jeemain,name='jeemain'),
    path('jeeadvance/',views.jeeadvance,name='jeeadvance'),
    path('neet/',views.neet,name='neet'),
    path('previousyear/',views.previousyear,name='previousyear'),
    path('ncert_chapter1/',views.ncert_chapter1,name='ncert_chapter1'),
    path('chapter/',views.chapter,name='chapter'),
    path('live/',views.live,name='live'),
]