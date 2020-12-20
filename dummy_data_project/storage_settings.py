import environ
import os
from pathlib import Path

env = environ.Env()

environ.Env.read_env(env_file='.env')

BASE_DIR = Path(__file__).resolve().parent.parent

# Boto3
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# AWS
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETRES = {'CacheControl': 'max-age=86400'}
# A path prefix that will be prepended to all uploads
AWS_LOCATION = 'static/'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}'
# Django static file directory
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
