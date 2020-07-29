from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('HomeView',HomeView ,name='HomeView' ),
    path('generate',on_generate,name='generate'),
    ]

