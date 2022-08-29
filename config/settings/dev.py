import os

os.environ.setdefault('DJANGO_SECRET_KEY', '{{ secret_key }}')

os.environ.setdefault('DATABASE_HOST', 'localhost')
os.environ.setdefault('DATABASE_PORT', 5432)
os.environ.setdefault('DATABASE_NAME', '{{ project_name }}_db')
os.environ.setdefault('DATABASE_USER', '{{ project_name }}_user')
os.environ.setdefault('DATABASE_PASSWORD', '{{ project_name }}_password')

from .base import *

DEBUG = True

THIRD_PARTY_APPS += [
    'django_debug_toolbar',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS
