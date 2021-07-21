from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Home(request):
    return render(request, 'home.html')


def News(request):
    return render(request, 'news.html')


def Contact(request):
    return render(request, 'contact.html')
