"""
Django settings for ffw project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # installed applications
    'rest_framework',
    # SIB applications
    'products',
    'filters',
    'cart',
    # 'export',
    # main module
    'main.assembly',
    'main.sibadmin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    "django.contrib.messages.context_processors.messages",
    # custom
    "products.context_processors.categories"
)


TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'frontend', 'templates'),
    os.path.join(PROJECT_DIR, 'frontend', 'templates-examples'),
)

ROOT_URLCONF = 'main.server.urls'

WSGI_APPLICATION = 'main.server.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(PROJECT_DIR, 'locale'),
)

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'collected_static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'frontend', 'static'),
    os.path.join(PROJECT_DIR, 'main', 'assembly', 'static'),
)


# *************************** APPLICATIONS SETTINGS *************************** #

FILTERS = {
    'Product': 'products.Product',
    'Category': 'products.Category',
    'Characteristic': 'products.Characteristic',
}

EXPORT = {
    'Product': 'products.Product',
}

CART = {
    'Product': 'products.Product',
    'product_price': 'price',
    'product_code': 'code',
    'product_name': 'name',
}
