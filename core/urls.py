from django.conf.urls import url
from django.urls import path
from .views import homepage


urlpatterns = [
    path('', homepage, name="homepage"),
]
