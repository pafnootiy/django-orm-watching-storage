import os
from dotenv import load_dotenv
from environs import Env
import argparse

env = Env()
env.read_env()
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv("HOST"),
        'PORT': os.getenv("PORT"),
        'NAME': os.getenv("NAME"),
        'USER': os.getenv("USER"),
        'PASSWORD': os.getenv("PASSWORD"),
    }
}

parser = argparse.ArgumentParser(
    description='Описание что делает программа'
)
parser.add_argument('HOST', help='Ваш хост')
parser.add_argument('--PORT', help='Номер порта', type=int)
parser.add_argument('--NAME', help='Ваше имя')
parser.add_argument('--USER', help='Ваш логин')
parser.add_argument('--PASSWORD', help='Ваш пароль')
args = parser.parse_args()
print("HOST", args.HOST)
print('PORT', args.PORT)
print('NAME', args.NAME)
print('USER', args.USER)
print('PASSWORD', args.PASSWORD)

INSTALLED_APPS = ['datacenter']
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG")
ROOT_URLCONF = 'project.urls'
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
