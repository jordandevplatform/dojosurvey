from django.http.response import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')

def create(request):
    request.session['dog_name'] = request.POST['dog_name']
    request.session['dog_breed'] = request.POST['dog_breed']
    request.session['dog_tricks'] = request.POST['dog_tricks']
    request.session['comment'] = request.POST['comment']
    
    return redirect('/result')

def result(request):
    context= {
        'dog_name': request.session['dog_name'],
        'breed' : request.session['dog_breed'],
        'trick' : request.session['dog_tricks'],
        'comment' : request.session['comment']
    }
    return render(request, 'dog.html', context)