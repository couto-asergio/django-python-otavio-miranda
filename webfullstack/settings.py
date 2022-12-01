# coding=utf-8

"""
Django settings for class_based_view project.
"""
import os
from pathlib import Path

from django.contrib.messages import constants

# from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = "django-insecure-()vk@w-t8ye(7-&61wfke8x7m_p2+ywhm#&6(-&6oy+^36o5dq"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # libs

    # apps
    'authors',
    'recipes',
    'debug_toolbar',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "webfullstack.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / 'base_templates',
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "webfullstack.wsgi.application"

# Ignore long line error flake8(E501)--> # noqa: E501
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},  # noqa: E501
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},  # noqa: E501
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},  # noqa: E501
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},  # noqa: E501
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Directory that will contain the static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = "static/"
STATICFILES_DIRS = ['static']
# STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Extra security features of Django
SECURE_HSTS_SECONDS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# Run only HTTPS server.
# Type Heroku etc.
# SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MESSAGE_TAGS = {
    constants.DEBUG: 'message-debug',
    constants.ERROR: 'message-error',
    constants.INFO: 'message-info',
    constants.SUCCESS: 'message-success',
    constants.WARNING: 'message-warning',
}

# Debug Toolsbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Import file local settings
try:
    from .local_settings import *
except ImportError:
    pass
