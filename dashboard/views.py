from django.shortcuts import render, redirect
from django.contrib import messages
from .models import News
from .forms import RegistrationForm
from .models import RegistrationData

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
    return render(request, 'news-1.html', context)


def Contact(request):
    return render(request, 'contact.html')


def SignUp(request):
    context = {
        "form": RegistrationForm
    }
    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      email=form.cleaned_data['email'],
                                      phone=form.cleaned_data['phone'])
        myregister.save()
        messages.add_message(request, messages.SUCCESS,
                             "You have signup successfully!")

    return redirect('signup')
