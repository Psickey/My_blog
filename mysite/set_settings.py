# Settings for deploy or Dev

import os
import socket

dev_machine = ('Psicks')

if socket.gethostname() in dev_machine:
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'blog',
            'USER': 'postgres',
            'PASSWORD': 'admin',
        }
    }

    SESSION_COOKIE_SECURE = False

    CSRF_COOKIE_SECURE = False

    SECURE_REFERRER_POLICY = 'origin'

    SECURE_SSL_REDIRECT = False
else:
    DEBUG = False

    DATABASES = {
        'default': {'ENGINE': os.environ.get('DB_ENGINE'),
                    'NAME': os.environ.get('DB_NAME'),
                    'USER': os.environ.get('DB_USER'),
                    'PASSWORD': os.environ.get('DB_PASSWORD'),
                    'HOST': os.environ.get('DB_HOST'),
                    'PORT': '5432'}
    }

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_REFERRER_POLICY = 'origin'

    SECURE_SSL_REDIRECT = True


