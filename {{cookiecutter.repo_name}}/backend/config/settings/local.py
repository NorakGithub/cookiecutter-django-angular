from .base import *


SECRET_KEY = '8m1)-&p0h$bh0b6ouk%+ifhcs5995&o$atv4hmt(vk$tl15+*u'
DEBUG = True
ALLOWED_HOSTS = ['*']

# App specifically for development
INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

# Middleware for development
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]
