from base import *
from modules import INSTALLED_MODULES

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pipeline',
)

for module in INSTALLED_MODULES:
    INSTALLED_APPS += ('%s.%s' % ('.'.join(segment for segment in MODULE_LOCATION), module),)