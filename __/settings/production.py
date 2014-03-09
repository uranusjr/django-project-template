#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Settings for deployment.
"""

from .base import *     # noqa

try:
    server_address = get_environ('{{ project_name|upper }}_ADDRESS')
except ImproperlyConfigured:
    pass
else:
    ALLOWED_HOSTS.append(server_address)

try:
    server_ip = get_environ('{{ project_name|upper }}_SERVER_IP')
except ImproperlyConfigured:
    pass
else:
    ALLOWED_HOSTS.append(server_ip)

ADMINS = (
    ('Tzu-ping Chung', 'uranusjr@gmail.com'),
)

SECRET_KEY = get_environ('{{ project_name|upper }}_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_environ('{{ project_name|upper }}_DB_DEFAULT_NAME'),
        'USER': get_environ('{{ project_name|upper }}_DB_DEFAULT_LOGIN'),
        'PASSWORD': get_environ('{{ project_name|upper }}_DB_DEFAULT_PASSWORD'),
        'HOST': get_environ('{{ project_name|upper }}_DB_DEFAULT_HOST'),
        'PORT': get_environ('{{ project_name|upper }}_DB_DEFAULT_PORT'),
    },
}

STATIC_ROOT = get_environ('{{ project_name|upper }}_STATIC_ROOT')

MEDIA_ROOT = get_environ('{{ project_name|upper }}_MEDIA_ROOT')

# Email settings with Gmail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_environ('{{ project_name|upper }}_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_environ('{{ project_name|upper }}_EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
