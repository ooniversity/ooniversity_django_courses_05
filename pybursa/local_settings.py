"""
Django settings for pybursa project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '50g@m(%2-%&rk#k#ym$(5##ex5$tn$k61apf-oc=^s%__5m12^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
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




ADMINS = [('admin', 'vivid.tanya@gmail.com'), ('tatyana_paschenko', 'vivid.tanya@gmail.com')]

EMAIL_HOST = 'smtp.sendgrid.net'

EMAIL_PORT = '587'

EMAIL_HOST_USER = 'tatyana_paschenko'

EMAIL_HOST_PASSWORD = '8074vivid8074'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers':
        {
            'courses': {
                'handlers': ['file1'],
                'level': 'DEBUG',
            },

            'students': {
                'handlers': ['file2'],
                'level': 'WARNING',
            },
        },
    'handlers':
        {
            'file1': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'simple',
                'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
            },
            'file2': {
                'level': 'WARNING',
                'class': 'logging.FileHandler',
                'formatter': 'verbose',
                'filename': os.path.join(BASE_DIR, 'students_logger.log'),
            },
        },
}
