from .base import *

DEBUG = bool(os.getenv("DEBUG"))

IS_ENV = 'DEV'

ALLOWED_HOSTS = ['localhost','127.0.0.1', '']

INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

# Test Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

STATIC_URL = '/static/'

BASE_PATH = os.path.join(BASE_DIR)

STATICFILES_DIRS = [os.path.join(BASE_PATH, 'resume/static')]

STATIC_ROOT = os.path.join(BASE_PATH, 'resume/static/includes')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_PATH, 'resume/static/media')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

print("\n")
print("DEBUG = ", DEBUG)
print("MODE = ", IS_ENV)
print("DATABASES = ", DATABASES['default']['NAME'])
print("HOST = ", DATABASES['default']['ENGINE'])
print("TEMPLATES = ", TEMPLATES[0]['DIRS'])
print("STATIC_ROOT = ", STATIC_ROOT)
print("MEDIA_ROOT = ", MEDIA_ROOT)
print("\n")