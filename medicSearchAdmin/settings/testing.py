from .settings import *

DEBUG = True

SECRET_KEY = 'ajfn9820p3irjnpfsnpi09I-JI09NOP)(OKJ_)nu-0kpoj20-o'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    }
}