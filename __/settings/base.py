#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django settings for {{ project_name }}.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def get_environ(key):
    try:
        return os.environ[key]
    except KeyError:
        raise ImproperlyConfigured(
            'Environment variable {key} required.'.format(key=key)
        )


DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []
INTERNAL_IPS = ('127.0.0.1',)


# Application definition

INSTALLED_APPS = (
    'base',
    'south',
    'compressor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = '__.urls'

WSGI_APPLICATION = '__.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


# Meddia files

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

MEDIA_URL = '/media/'


# Tastypie

TASTYPIE_DEFAULT_FORMATS = ["json"]
