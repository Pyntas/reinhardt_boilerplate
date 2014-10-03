"Local isolated configuration"
from __future__ import absolute_import
import os

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


DEBUG = True

TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1',)
SECRET_KEY = get_env_setting("SETTINGS_KEY")

#Google analytics trancking
ANALYTICS_TRACKING_ID = 'UA-XXXXXXX-XX'
