import dj_database_url 

from .base import *


DEBUG = not bool(os.getenv("DEBUG"))

IS_ENV = 'PRODUCTION'

ALLOWED_HOSTS = ['localhost', '127.0.0.1' , '']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Honor the 'X-Forwarded-Proto' header fro request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}

STATIC_URL = '/static/'

BASE_PATH = os.path.join(BASE_DIR)

STATICFILES_DIRS = [os.path.join(BASE_PATH, 'resume/static')]

STATIC_ROOT = os.path.join(BASE_PATH, 'resume/static/includes')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_PATH, 'resume/static/media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

print("\n")
print("DEBUG = ", DEBUG)
print("MODE = ", IS_ENV)
print("STATIC_ROOT = ", STATIC_ROOT)
print("MEDIA_ROOT = ", MEDIA_ROOT )
print("\n")
