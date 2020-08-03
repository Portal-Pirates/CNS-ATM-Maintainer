import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



INSTALLED_APPS = [
    'core.apps.SuitConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', 
    'NewEntry',
    'admin_reorder',
    'accounts.apps.AccountsConfig',
    'managerView'
    
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',#reorder middleware
]

ROOT_URLCONF = 'CNS-ATM-Maintainer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
    }
}


# Reordering Settings
ADMIN_REORDER = (
    # Keep original label and models
    'sites',

    # Rename app
    {'app': 'auth', 'models': ('auth.User', 'auth.Group', 'core.Profile'), 'label': 'Permissions & Accounts'},
  
    # Reorder app models
     {'app': 'core', 'models': ('core.Airports', 'core.Stations', 'core.Equipments'), 'label': 'Airports & Stations'},
    {'app': 'core', 'models': ('core.COMSOFT', 'core.VCS_System', 'core.Glid_Path', 'core.Localizer', 'core.DVOR', 'core.NDB', 'core.Datis_Terma', 'core.DVTR', 'core.UPS', 'core.OtherEquipmentsReport'), 'label': 'Equipment Reports'},
    
)

#Settings for email sending apis
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER ='ac7908840@gmail.com'
EMAIL_HOST_PASSWORD = 'abcd*12345'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

import django_heroku
django_heroku.settings(locals())
