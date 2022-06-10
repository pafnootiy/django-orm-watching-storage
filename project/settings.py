import os
from dotenv import load_dotenv
from environs import Env

env = Env()
env.read_env()

load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASSWORD")
secret_key = os.getenv("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': user,
        'PASSWORD': password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

# env.bool("DEBUG")
# debug = env("DEBUG")
DEBUG = env.bool("DEBUG")
ROOT_URLCONF = 'project.urls'
# DEBUG = True
print(DEBUG)
ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
