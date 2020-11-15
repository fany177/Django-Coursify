from django.shortcuts import render

def home(request):
    return render(request,'Application/home.html')

def course(request):
    return render(request,'Application/course.html')

def board(request):
    return render(request,'Application/board.html')

def book(request):
    return render(request,'Application/book.html')

def book1(request):
    return render(request,'Application/book1.html')

def book2(request):
    return render(request,'Application/book2.html')

def book3(request):
    return render(request,'Application/book3.html')

def join(request):
    return render(request,'Application/join.html')

def video(request):
    return render(request,'Application/video.html')




def boardexams(request):
    return render(request,'Application/boardexams.html')

def schoolexams(request):
    return render(request,'Application/schoolexams.html')


def jeemain(request):
    return render(request,'Application/jeemain.html')

def jeeadvance(request):
    return render(request,'Application/jeeadvance.html')

def neet(request):
    return render(request,'Application/neet.html')

def previousyear(request):
    return render(request,'Application/previousyear.html')

def ncert_chapter1(request):
    return render(request,'Application/ncert_chapter1.html')


def chapter(request):
    return render(request,'Application/chapter.html')

def live(request):
    return render(request,'Application/live.html')
