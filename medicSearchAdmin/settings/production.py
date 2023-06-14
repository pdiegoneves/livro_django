from .settings import *

DEBUG = False

SECRET_KEY = 'asdkf2co80i9ok,3flçmsnp9d890jomNp*(u+)_oJNOIUN-9U=mkon2k'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    }
}