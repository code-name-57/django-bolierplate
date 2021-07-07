from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s7uftu0#o+x7f_ane(1(o=r1xx7nr=-yu%0yl-!gp%$!l0v0oz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Media files (user uploads, images, videos etx)
MEDIA_ROOT= BASE_DIR.joinpath('media/')
MEDIA_URL= "/media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'


ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


