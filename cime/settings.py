"""
Configuración CIME-Core

guía:
https://docs.djangoproject.com/en/1.11/topics/settings/
referencia:
https://docs.djangoproject.com/en/1.11/ref/settings/
django-environ:
https://django-environ.readthedocs.io/
"""

import environ
import os

# Directorio base de la aplicación
__root = environ.Path(__file__) - 2
BASE_DIR = __root()

# Cargar ambiente
# Leer el README.md: mover .env.ejemplo a .env
__env = environ.Env()
__env.read_env(__root('.env'))

DEBUG = __env('DEBUG', cast = bool, default = False)

# Seguridad
# TODO configurar seguridad: estas configuraciones no son ideales para
# ambientes de produccion. Leer más:
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
SECRET_KEY = __env('SECRET_KEY')
ALLOWED_HOSTS = __env('ALLOWED_HOSTS', cast = list, default = [])
X_FRAME_OPTIONS = __env('X_FRAME_OPTIONS', cast = str, default = 'DENY')
CSRF_COOKIE_SECURE = __env('CSRF_COOKIE_SECURE', cast = bool, default = False)
SESSION_COOKIE_SECURE = __env('SESSION_COOKIE_SECURE', cast = bool,
    default = False)
SECURE_SSL_REDIRECT = __env('SECURE_SSL_REDIRECT', cast = bool, default = False)
SECURE_BROWSER_XSS_FILTER = __env('SECURE_BROWSER_XSS_FILTER', cast = bool,
    default = False)
SECURE_CONTENT_TYPE_NOSNIFF = __env('SECURE_CONTENT_TYPE_NOSNIFF', cast = bool,
    default = False)
SECURE_HSTS_SECONDS = __env('SECURE_HSTS_SECONDS', cast = int, default = 0)

# Aplicaciones del Framework
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Aplicaciones Externas
VENDOR_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

# Aplicaciones Internas
CIME_APPS = []

# Aplicaciones Instaladas...
INSTALLED_APPS = DJANGO_APPS + VENDOR_APPS + CIME_APPS

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cime.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'cime.wsgi.application'

# Bases de datos y cache
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': __env.db()
}

# Validadores de contraseña
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
__validator_module = 'django.contrib.auth.password_validation'
__validator_classes = ['UserAttributeSimilarityValidator',
    'MinimumLengthValidator', 'CommonPasswordValidator',
    'NumericPasswordValidator']

AUTH_PASSWORD_VALIDATORS = [
    dict(NAME='{0}.{1}'.format(__validator_module, validator))
    for validator in __validator_classes ]

# Internacionalización y localización
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = __env('STATIC_URL', cast = str, default = '/static/')
