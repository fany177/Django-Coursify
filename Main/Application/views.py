from django.shortcuts import render

def home(request):
    return render(request,'Application/home.html')


def live(request):
    return render(request,'Application/live.html')

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


def book(request):
    return render(request,'Application/book.html')

def book1(request):
    return render(request,'Application/book1.html')

def ncert(request):
    return render(request,'Application/ncert.html')

def chapter1(request):
    return render(request,'Application/chapter1.html')

def exercise(request):
    return render(request,'Application/exercise.html')

def question(request):
    return render(request,'Application/question.html')


def course(request):
    return render(request,'Application/course.html')

def join(request):
    return render(request,'Application/join.html')

def board(request):
    return render(request,'Application/board.html')

def profile(request):
    return render(request,'Application/profile.html')
