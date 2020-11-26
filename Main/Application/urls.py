from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    path('welcome/',views.welcome,name='welcome'),
    
    path('result/',views.result,name='result'),
    path('video/',views.video,name='video'),
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
    path('question/<str:video_id>/<str:video_title>/<path:t>',views.question,name='question' ),
    
    path('course/',views.course,name='course'),
    path('join/',views.join,name='join'),
    
    path('board/',views.board,name='board'),
    
    path('profile/',views.profile,name='profile'),
    
    path('drop/',views.drop,name='drop'),
    
]