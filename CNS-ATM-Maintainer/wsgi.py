import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CNS-ATM-Maintainer.settings.development')

application = get_wsgi_application()
application = WhiteNoise(application, root='static_files')

