from django.urls import path
from .views import Home, NewsP, Contact

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact')
]
