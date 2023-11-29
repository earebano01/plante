from django.urls import path
from .views import BASE
urlpatterns = [
    path('', BASE, name='BASE'),

]