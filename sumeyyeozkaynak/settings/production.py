from sumeyyeozkaynak.settings.base import *

DEBUG = False
ALLOWED_HOSTS=['www.sumeyyeozkaynak.me', 'sumeyyeozkaynak.me','188.166.122.13']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_website',
        'USER': 'sumeyyeozkaynak',
        'PASSWORD': '203948',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

NOCAPTCHA = True
