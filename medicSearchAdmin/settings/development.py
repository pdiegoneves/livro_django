from .settings import *


DEBUG = True

SECRET_KEY = 'akmksmdpaokm0diokapowkdoakcpmlxkzm cokpqm=pok´plm'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    }
}

