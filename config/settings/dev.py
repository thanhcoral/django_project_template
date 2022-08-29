from .base import *

DEBUG = True

THIRD_PARTY_APPS += [
    # 'django_debug_toolbar',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS
