from .settings import *

DEBUG = True

SECRET_KEY = 'ajfn9820p3irjnpfsnpi09I-JI09NOP)(OKJ_)nu-0kpoj20-o'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    }
}