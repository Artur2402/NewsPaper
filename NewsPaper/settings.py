"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hd15gtys0chm!@#sq&-o##%4%dci6cmh82dd4uog2mdf6!(rr4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news',
    'accounts',
    'fpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignUpForm"}
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "nogerovarthur24"
EMAIL_HOST_PASSWORD = "cjbhqooxxzatpfdj"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "nogerovarthur24@yandex.ru"

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static']

LOGIN_REDIRECT_URL = "/news"

# D13 Логирование

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug_console': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },

        'warning_console': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'error_critical': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'general_sec_log': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'mail': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        }
    },

    'filters': {  # 5
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug_console'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_console'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_critical'
        },
        'general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general_sec_log'
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'general_sec_log'
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_critical'
        },
        'critical': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_critical'
        },
        'mail_admin': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mail'
        }
    },

    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'general', 'console_error'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errors', 'critical'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['errors', 'critical'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors', 'critical', 'mail_admin'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errors', 'critical', 'mail_admin'],
            'propagate': True,
        }
    }
}
