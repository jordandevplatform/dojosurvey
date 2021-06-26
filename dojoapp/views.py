from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    context= {
        'dog_name': request.POST['dog_name'],
        'breed' : request.POST['dog_breed'],
        'trick' : request.POST['dog_tricks'],
        'comment' : request.POST['comment']
    }
    return render(request, 'dog.html', context)