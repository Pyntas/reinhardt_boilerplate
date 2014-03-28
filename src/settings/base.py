# -*- coding: utf-8 -*-

# from os.path import abspath, basename, dirname, join, normpath
# from sys import path
from unipath import Path


from django.utils.translation import ugettext_lazy as _

# Absolute filesystem path to the Django project directory:
# DJANGO_ROOT = dirname(dirname(abspath(__file__)))
# # Absolute filesystem path to the top-level project folder:
# SITE_ROOT = dirname(DJANGO_ROOT)

# SITE_NAME = basename(DJANGO_ROOT)
# # Add our project to our pythonpath, this way we don't need to type our project
# # name in our dotted import paths:
# path.append(DJANGO_ROOT)

PROJECT_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'x0ti!-l45vv5tjl^r&o8e#l36xlv*)tv8qo(^m+u4s9)9m4=th'

SITE_URL = "http://local.example.com:8000"

DEBUG = False
TEMPLATE_DEBUG = DEBUG

#See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins & #managers
ADMINS = (
    ('Hello my name is', 'your_email@example.com'),
)
MANAGERS = ADMINS



ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'


DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'core',
    'web',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'core.context_processors.analytics',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    PROJECT_DIR.child('src', 'templates'),
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR.child('db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)
LOCALE_PATHS = (
    PROJECT_DIR.child('src').child('locale'),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_ZONE = 'Europe/Madrid'

# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_ROOT = PROJECT_DIR.child('media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'


# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = PROJECT_DIR.child('assets')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



INSTALLED_APPS += (
    'south',
    'django_nose',
)

# Don't need to use South when setting up a test database.
SOUTH_TESTS_MIGRATE = False

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ['--cover-test' ,'--with-doctest' ,'--with-yanc', '--verbosity=2']

#Google analytics trancking
ANALYTICS_TRACKING_ID = 'UA-XXXXXXX-XX'
