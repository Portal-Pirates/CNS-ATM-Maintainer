from django.conf.urls import url
from django.urls import path
from .views import NewEntry


urlpatterns = [
    path('', NewEntry, name="NewEntry"),
]
