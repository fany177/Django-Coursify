import requests
from urllib.parse import quote
from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect


def welcome(request):
    return render(request,'Application/welcome.html')

def home(request):

    videos = []

    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 10,
            'type' : 'video',
            'channelId': 'UCM2zKwI6dlR46sSnkkWRMnQ'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 10
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        
        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)

        context = {
            'videos' : videos
        }

        return render(request,'Application/result.html', context)
    return render(request,'Application/home.html')

def result(request):
    return render(request,'Application/result.html')

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

def question(request,video_id,video_title,t):
    link = {"link":'https://www.youtube.com/embed/'+video_id, 'title':video_title, 't':t}
    return render(request,'Application/question.html',link)


def course(request):
    return render(request,'Application/course.html')

def join(request):
    return render(request,'Application/join.html')

def board(request):
    return render(request,'Application/board.html')

def profile(request):
    return render(request,'Application/profile.html')

def drop(request):
    return render(request,'Application/drop.html')

def video(request):
    return render(request,'Application/video.html')
