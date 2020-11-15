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
    path('book/book_list/',views.book_list,name='book_list'),
    path('book/book_list/ncert/',views.ncert,name='ncert'),
    path('book/book_list/ncert/ncert_chapter1/',views.ncert_chapter1,name='ncert_chapter1'),
    path('book/book_list/ncert_chapter1/ncert_chapter1_exercise/',views.ncert_chapter1_exercise,name='ncert_chapter1_exercise'),
    path('book/book_list/ncert_chapter1/ncert_chapter1_exercise/1uestion',views.question,name='question'),
    
    path('course/',views.course,name='course'),
    path('join/',views.join,name='join'),
    
    path('board',views.board,name='board'),
    
  
   
    
    
    # path('chapter1/',views.chapter1,name='chapter1'),
    # path('video/',views.video,name='video'),
   
    
    
    
]