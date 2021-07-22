from django.urls import path
from .views import Home, NewsP, Contact, SignUp, addUser

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact'),
    path('signup/', SignUp, name='signup'),
    path('addUser', addUser, name='addUser')
]
