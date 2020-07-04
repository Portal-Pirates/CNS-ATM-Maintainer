from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import django.views.static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
   url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG})
]
