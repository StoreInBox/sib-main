from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x*m*9+#t04u3*80t@phqqh)&q9=do)ot1fjz^s#h5r5wweag8b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ['http://127.0.0.1:8000']

TEMPLATE_DEBUG = DEBUG

LANGUAGE_CODE = 'en'

ALLOWED_HOSTS = []

# MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'ffw',                         # Or path to database file if using sqlite3.
#         'USER': 'ffw_user',                    # Not used with sqlite3.
#         'PASSWORD': 'ffw_password',            # Not used with sqlite3.
#         'HOST': '127.0.0.1',                   # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                            # Set to empty string for default. Not used with sqlite3.
#     }
# }

# SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join('db.sqlite3'),                         # Or path to database file if using sqlite3.
    }
}
