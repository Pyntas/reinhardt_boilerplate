# -*- coding: utf-8 -*-
"Local isolated configuration"
from __future__ import absolute_import
import os

from .base import *

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        pass


DEBUG = True
TEMPLATE_DEBUG = DEBUG
TESTING = True

SECRET_KEY = get_env_setting("SECRET_KEY")

INTERNAL_IPS = ('127.0.0.1',)

SITE_URL = "http://localhost:8000"

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--cover-test' ,'--with-doctest' ,'--with-yanc', '--verbosity=2', ]


EMAIL_SENDER = 'Django Reinhardt<django@email.com>'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


TIME_ZONE = 'Europe/Madrid'

INTERNAL_IPS = ('127.0.0.1',)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'analytics': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

from web.settings import *
