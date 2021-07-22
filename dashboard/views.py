from django.shortcuts import render
from .models import News

# Create your views here.


def Home(request):
    context = {
        "name": "Alexey Grigorev",
        "number": "1994"
    }
    return render(request, 'home.html', context)


def NewsP(request):
    obj = News.objects.get(id=1)
    context = {
        "data": obj
    }
    return render(request, 'news.html', context)


def Contact(request):
    return render(request, 'contact.html')


def SignUp(request):
    return render(request, 'signup.html')
