from __future__ import absolute_import, unicode_literals

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']


from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

AWS_S3_REGION_NAME = 'us-east-1'
AWS_STORAGE_BUCKET_NAME = 'isawebsite'
AWS_ACCESS_KEY_ID = env['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = env['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_HOST = 's3.amazonaws.com'
S3_USE_SIGV4 = True
AWS_QUERYSTRING_AUTH = False


MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = env['EMAIL_HOST_PASSWORD']

WAGTAIL_ADDRESS_MAP_KEY = env['WAGTAIL_ADDRESS_MAP_KEY']
WAGTAIL_ADDRESS_MAP_CENTER = 'Charing Cross Hospital, London, United Kingdom'  # It must be a properly formatted address

# Optional
WAGTAIL_ADDRESS_MAP_ZOOM = 14  # See https://developers.google.com/maps/documentation/javascript/tutorial#MapOptions for more information.
WAGTAIL_ADDRESS_MAP_LANGUAGE = 'en'  # See https://developers.google.com/maps/faq#languagesupport for supported languages.

#twiiter api tokens
consumer_token = env['CONSUMER_KEY']
consumer_secret = env['CONSUMER_SECRET']
access_token = env['ACCESS_TOKEN']
access_token_secret = env['ACCESS_TOKEN_SECRET']
