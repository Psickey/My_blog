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
    DEBUG = True

    DATABASES = {'default': {} }

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_REFERRER_POLICY = 'origin'

    SECURE_SSL_REDIRECT = True


