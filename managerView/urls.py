from django.urls import path
from .views import *

urlpatterns = [
    path("showmanager",getManagerProfile,name="showmanager")
]