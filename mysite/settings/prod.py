from mysite.settings.base import *

import django_on_heroku



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

ALLOWED_HOSTS = ['rugviz.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Media files (user uploads, images, videos etx)
DROPBOX_OAUTH2_TOKEN = os.environ['DROPBOX_OAUTH2_TOKEN']

DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

MEDIA_ROOT=     os.path.join(BASE_DIR, 'mysite/media'),

MEDIA_URL= "/media/"

django_on_heroku.settings(locals())