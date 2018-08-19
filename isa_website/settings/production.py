from __future__ import absolute_import, unicode_literals

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']


from .base import *

DEBUG = False

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

AWS_STORAGE_BUCKET_NAME = env['BUCKET_NAME']
AWS_S3_REGION_NAME = env['REGION_NAME']
AWS_ACCESS_KEY_ID = env['ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = env['SECRET_ACCESS_KEY']
DEFAULT_FILE_STORAGE = env['DEFAULT_FILE_STORAGE']
AWS_S3_HOST = env['AWS_S3_HOST']
S3_USE_SIGV4 = env['S3_USE_SIGV4']
