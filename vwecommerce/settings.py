"""
Django settings for vwecommerce project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/

Quick-start development settings - unsuitable for production
https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
"""

import os
import dj_database_url

# Armazena o diretorio raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Criar variável de ambiente para armazenar o secret_key
# Usado para fazer a criptografia da sua senha
SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET_KEY_DEFAULT')

# Modo de debug para ambiente de desenvolvimento, deve ser False quando colocado em produção
DEBUG = False

# Dominios permitidos para a aplicação
ALLOWED_HOSTS = []

# Instalar aplicações
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'model_mommy',
    'rest_framework',
    'core',
    'accounts',
    'catalog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vwecommerce.urls'

# Sistema de templates
# BACKEND: É o sistema principal de templates do django
# DIRS: Lista de diretorios onde irei encontrar meus templates
# APP_DIRS: Indica que cada aplicação terá seus templates
# Context_processors: São funções que são chamadas toda vez que um template for renderizado
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'catalog.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'vwecommerce.wsgi.application'

# Banco de Dados
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# ENGINE: é o banco de dados que irá utilizar
# NAME: é onde será armazenado o banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Validação de senhas
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Sistema de internacionalização
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
# Lugares extras para o django achar arquivos estaticos.
STATICFILES_DIRS = (
  os.path.join(PROJECT_ROOT, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Database
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Configurações de segurança do heroku
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Permitir todos os dominios que vão ter acesso a essa aplicação
ALLOWED_HOSTS = ['*']


# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Nome <victorhad@gmail.com>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'victorhad@gmail.com'
EMAIL_HOST_PASSWORD = '****'
EMAIL_PORT = 587
CONTACT_EMAIL = 'victorhad@gmail.com'

# AUTH
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'core:home'
LOGOUT_URL = 'accounts:logout'
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'accounts.backends.ModelBackend',
)

# Sobrescrever as configurações do settings.py com as do local_settings.py
try:
  from .local_settings import *
except ImportError:
  pass
