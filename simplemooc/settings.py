# -*- coding: utf-8 -*-
"""
Django settings for simplemooc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1oyox#pauu2n*eyc)qc@k51w!xylesaj53vp(9=exguvyfhe79'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Extra apps
    'django_extensions',  # run python manage.py shell_plus :)

    # my apps
    'simplemooc.core',
    'simplemooc.accounts',
    'simplemooc.courses',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'simplemooc.urls'

WSGI_APPLICATION = 'simplemooc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# O media root é util para que voce crie configurações de upload de arquivos
MEDIA_ROOT = os.path.join(BASE_DIR, 'simplemooc', 'media')
MEDIA_URL = '/media/'  # esta constante é referente aos arquivos de media, que foram feito uploads pelo usuario

# envio de emails.
# EMAIL BACKEND
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # back end para o console.
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # back end para o gmail
# DEFAULT_FROM_EMAIL = 'Nome <email@gmail.com>'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'email@gmail.com'
# EMAIL_HOST_PASSWORD = 'senha'
# EMAIL_PORT = 587

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # com este cara a gente faz um email de teste no console.
DEFAULT_FROM_EMAIL = 'nome <email@gmail.com>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email@gmail.com'
EMAIL_HOST_PASSWORD = 'senha'
EMAIL_PORT = 587

CONTACT_EMAIL = 'anderson.araujoprog@gmail.com'

# Auth Configs

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'core:home'
LOGOUT_URL = 'accounts:logout'
