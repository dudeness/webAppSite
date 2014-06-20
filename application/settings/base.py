"""
Django settings for webAppSite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))[0]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition

ROOT_URLCONF = 'application.urls'

WSGI_APPLICATION = 'application.settings.wsgi.application'


MODULE_LOCATION = ('application', 'modules')
MODULE_PATH = os.path.join(PROJECT_PATH, os.sep.join(segment for segment in MODULE_LOCATION))


