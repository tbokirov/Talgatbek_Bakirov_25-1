from django.shortcuts import redirect, HttpResponse
import time

def youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com')

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse ('Hello! Its my project')

def google_view(request):
    if request.method == 'GET':
        return redirect('https://www.google.com')

def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')

def now_date_b_view(request):
    if request.method == 'GET':
        now = time.strftime("%Y-%m-%d")
        html = "<html><body>Сейчас %s.</body></html>" % now
        return HttpResponse(html)