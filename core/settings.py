import os
from pathlib import Path
from typing import List

BASE_DIR = Path(os.environ.get('DJANGO_SETTINGS_BASE_PATH', '.')).resolve()
DEBUG = True
SECRET_KEY = 'django-insecure-v9bm30@ks616z((_-v0z8^3@52fy(jw*^uoh@qe%hqhb_l+yal'

if 'INSTALLED_APPS' not in globals():
    INSTALLED_APPS: List[str] = []

INSTALLED_APPS = [  # noqa F405
    'apps.main.apps.MainConfig', 'apps.settings.apps.SettingsConfig', 'apps.route.apps.RouteConfig',
] + INSTALLED_APPS

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if 'TEMPLATES' not in globals():
    TEMPLATES: list = [{'DIRS': []}]

TEMPLATES[0]['DIRS'] += [BASE_DIR / 'static/templates']

if 'LOGGING' not in globals():
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
        },
        'loggers': {
            'vvecon': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        },
    }  # noqa F405

LOGGING['formatters']['colored'] = {  # type: ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['vvecon']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'  # noqa F405

# Media files (Images)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'  # noqa F405
