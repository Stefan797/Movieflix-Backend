from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret! ???
SECRET_KEY = 'django-insecure-q-!*_xsr30wn67wccb8ur!5^nevi%nhvl#kb(4=@ypfmqk(ugc'

DEBUG = True # False bei dem nächsten update auf dem Server

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]', 'stefan-jonas.developerakademie.org']

AUTH_USER_MODEL = 'user.CustomUser'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'user',
    'movies.apps.MoviesConfig',
    'corsheaders',
    'debug_toolbar',
    'django_rq',
    'notifications'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

REST_FRAMEWORK = {
   'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.IsAuthenticated',
   ],
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.SessionAuthentication',
       'rest_framework.authentication.TokenAuthentication',
       'rest_framework.authentication.BasicAuthentication',
   )
}

CACHE_TTL = 900

INTERNAL_IPS = [
    '127.0.0.1',
]

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': 360,
    },

    # 'with-sentinel': {
    #     'SENTINELS': [('localhost', 26736), ('localhost', 26737)],
    #     'MASTER_NAME': 'redismaster',
    #     'DB': 0,
    #     'PASSWORD': 'secret',
    #     'SOCKET_TIMEOUT': None,
    #     'CONNECTION_KWARGS': {
    #         'socket_connect_timeout': 0.3
    #     },
    # },
    # 'high': {
    #     'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0'), # If you're on Heroku
    #     'DEFAULT_TIMEOUT': 500,
    # },
    # 'low': {
    #     'HOST': 'localhost',
    #     'PORT': 6379,
    #     'DB': 0,
    # }
}

AUTH_USER_MODEL = 'user.CustomUser'
CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:5500',
    'http://localhost:5501',
    'http://localhost:8000'
)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "movieflix"
    }
}

ROOT_URLCONF = 'movieflix.urls'

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

WSGI_APPLICATION = 'movieflix.wsgi.application'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5501",
    "http://127.0.0.1:8000"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")