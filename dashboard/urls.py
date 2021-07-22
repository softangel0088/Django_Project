from django.urls import path
from .views import Home, NewsP, Contact, SignUp

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact'),
    path('signup/', SignUp, name='signup')
]
