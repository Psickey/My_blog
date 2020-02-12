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
        'default': {'ENGINE': os.environ('DB_ENGINE'),
                    'NAME': os.environ('DB_NAME'),
                    'USER': os.environ('DB_USER'),
                    'PASSWORD': os.environ('DB_PASSWORD'),
                    'HOST': os.environ('DB_HOST'),
                    'PORT': '5432'}
    }

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_REFERRER_POLICY = 'origin'

    SECURE_SSL_REDIRECT = True


