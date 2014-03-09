#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configs that dev settings on local machines base on.
"""

from .base import *     # noqa

DEBUG = True

SECRET_KEY = '{{ secret_key }}'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += (
    'debug_toolbar',
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--cover-package=base',
    '--with-coverage',
    '--cover-erase',
]
