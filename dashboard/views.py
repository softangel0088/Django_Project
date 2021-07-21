from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Home(request):
    text = """<h1>Welcome to this home page!</h1>"""
    return HttpResponse(text)


def News(request):
    text = """<h1>Welcome to my News page!</h1>"""
    return HttpResponse(text)


def Contact(request):
    text = """<h1>Welcome to my Contact page!</h1>"""
    return HttpResponse(text)
