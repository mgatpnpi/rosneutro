"""
Django settings for rno project.

Generated by 'django-admin startproject' using Django 1.8.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# >>> development settings
DEBUG = True

ALLOWED_HOSTS = ['localhost',]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7q$gxw_g00e(+nx5#7nm056b(4m(tj2s-9_fwfgg*v79(ck4^l'

# SECURITY WARNING: don't run with debug turned on in production!

EMAIL_PORT = 1025
EMAIL_HOST = 'localhost'

DEFAULT_FROM_EMAIL = 'noreply@rno.pnpi.spb.ru'
# <<< development settings overrided by localsettings.py
try:
    from localsettings import *
except:
    pass


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'redactor',
    'compressor',
    'captcha',
    'pages',
    'members',
    'news'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware'
)

ROOT_URLCONF = 'rno.urls'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
WSGI_APPLICATION = 'rno.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru'
LANGUAGES = (
('ru', _('Russian')),
('en', _('English')),
)
LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
)


USE_I18N = True

USE_L10N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

ARCHIVE_ROOT = os.path.join(BASE_DIR, 'archive')

REDACTOR_OPTIONS = {'lang': 'ru', 'plugins': ['scriptbuttons']}
REDACTOR_UPLOAD = 'uploads/'
REDACTOR_UPLOAD_HANDLER = 'redactor.handlers.UUIDUploader'

COMPRESS_ENABLED = True
COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_PRECOMPILERS = (
        ('text/less', 'lessc {infile} {outfile}'),
        )


CELERY_TASK_RESULT_EXPIRES=3600
CELERY_ANNOTATIONS = {
    'rno.tasks.send_email_message': {'limit_rate': '1/m'}
        }
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ENABLE_UTC = False
