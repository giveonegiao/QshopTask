"""
Django settings for Qshop project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tqs503%9dl(=@8i3r#9)jon%3b%rcgk5^gtffv&%y%1+00q0g('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Seller',
    'Buyer',
    'djcelery'
]

MIDDLEWARE = [
   # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "Qshop.middleware.MiddleWareTest",
    # 'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = 'Qshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Qshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)

# STATIC_ROOT=os.path.join(BASE_DIR,'static')#静态文件的根目录，和STATICFILES_DIRS，MEDIA_URL，MEDIA_ROOT有冲突

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static')














alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzcQPLSN0l0GlBABNUebMCvEYDQXLlDe++s1011pNZaIl/oxkSVoxYJQKkX3YKsbT3Mp8tCyf7d7SAiMyJWIeUA8Gmz723EraGFNTADyj5ohlQ2Q1Hx7WUKoZMlcG8g32SeqDgk6uRyVSruFyalH/8vwVGcb5mGzzL4TfzrYklffGv3RjkJ5IdT9vZROUZIUp+M+5PKU0OdpHC05rTpUbX5I1UjT+w8BzjfAnnWEnchGwtxe/VI9k288jyxKqdYeTpWhG8DaUtMzDFwipCz5pibO0UwAPu01w+WdSLIMiHZe6V3nJWMU9MtaWRWAneeo8mGbPwOoIvcewp9U2H8GwkQIDAQAB
-----END PUBLIC KEY-----"""

alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAzcQPLSN0l0GlBABNUebMCvEYDQXLlDe++s1011pNZaIl/oxkSVoxYJQKkX3YKsbT3Mp8tCyf7d7SAiMyJWIeUA8Gmz723EraGFNTADyj5ohlQ2Q1Hx7WUKoZMlcG8g32SeqDgk6uRyVSruFyalH/8vwVGcb5mGzzL4TfzrYklffGv3RjkJ5IdT9vZROUZIUp+M+5PKU0OdpHC05rTpUbX5I1UjT+w8BzjfAnnWEnchGwtxe/VI9k288jyxKqdYeTpWhG8DaUtMzDFwipCz5pibO0UwAPu01w+WdSLIMiHZe6V3nJWMU9MtaWRWAneeo8mGbPwOoIvcewp9U2H8GwkQIDAQABAoIBAQCDO5YKTeCgT4e1I5QstixQli+mrpmGcH9naf4pEzjlpyLgVB3qApIXbJPI8yAZODILUUFzkDp39XKvVk83NHrsyIiIHwJGwZ6TgSEgt4w5Dai38INI09wQGkxzpLmTS4BW6DDzvMa+LXmse7EDSkUZbdjvVc3+fw4isnYjWlu/IOC+Bsdjw6bvI09vvYehPpwzgHhuEwSsLX+LQsczWVO4OCadG/5K38C/SCuhD1TDV0Y0BDXVUdWk4TnunArhqCt6SgxmWUNrFWvDF1YSi8QuRh7drCBp4V1pb++4mwzcutfi4gzzgvc+9SlYAJaooo1mQfa/XW4L0JJOxiGj7P5ZAoGBAPWI5Rnl8wqY64xFqd7syXsgVrIeWpBqKpGtRq+N+yKAHSeiwU+dH7viy44dhy4IKC1chHYu//isUdASJ1YDT56S7iO2r1ucZzvy9Tk6x6rOM+K1yoz/2YLRx+IQaGRrmbOu+3f46ToZpK1bIVseyElGpE9MN/oUlip8muJZ0Or3AoGBANaJO9k2xWPKzByHdy/iJGHFkV4lm5qRYon80Sv7ANkmVT+6iKvKC/BNqYliSa1zfa88R7IXEj18iGuGHwaBUM3rmbZZhpNCzIDalcmjypNO3q7v9bcfciuz+vVRjlqfoduabnfaOzjTID6OPZTe+kZEbJDvdTS2TwtcSLF365a3AoGBAORRzijNCbobBT5FMXdY3Oqf4b50N2b/MmKQrKBm+NbWJ0ZKNFRiGbZPaVXX43JMp3+2/n4fqmuFYfaISwfSwGEG5GdVY69euyil/p6fKDiO0vTIc3e2Gn9pr+NpuolW/XB3EOQ5FDewzM9fZJ8k+r4Y8IXErHDiX9lWUXiWaI11AoGABEdKXUOdXiceOPduphLRfO2uv3zqhIOfvna/SSxBURNVoea7cQmfgVRbLDU8mOvztrnyCBgzsew44EQVfFC55tFrCFrytx8e6vbxA8tzb8qj4ENC2DsVUM/PEnNk7mO+m52R1GwSwEhdnUHC8qQbw6j7rUxJPxrfqq9Vd8yXczMCgYEAhhDzDkrKKCXHNhlGx+aVjWyF9GxZ206oahD1ZtM/lgkOYPdtWpaV8yHUbgUpKANWTQ4GdCy7ux2gCaZcG72HGnC/Ge1s6f3nn/k+1WAvBI78jxXfKjV9926o/MaHdufa+Rs3SOkwvauqIg39XoxyHwmmZX/JcrQNj4AVyNu5V54=
-----END RSA PRIVATE KEY-----"""


MESSAGE_URL = "http://106.ihuyi.com/webservice/sms.php?method=Submit"
DING_URL="https://oapi.dingtalk.com/robot/send?access_token=2d227acf9a074f360d4f1c6988b700d34a661455daf338fb030e6c10ad054d34"

import djcelery   #导入django-celery模块
djcelery.setup_loader()   #进行模块加载
BROKER_URL='redis://127.0.0.1:6379/1'  #任务容器地址，ridis数据库地址
CELERY_IMPORTS=('CeleryTask.tasks')  #具体的任务文件
CELERY_TIMEZONE='Asia/Shanghai'  #celery时区
CELERYBEAT_SCHEDULER='djcelery.schedulers.DatabaseScheduler'  #celey处理器，固定


from celery.schedules import timedelta
from celery.schedules import crontab
CELERYBEAT_SCHEDULE={
    u'测试任务1':{
        "task":"CeleryTask.tasks.sendDing",#任务函数
        "schedule":timedelta(seconds=3)#执行时间
    }
}
ERROR_PATH=os.path.join(BASE_DIR,"error.log")



# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION':[
#             "127.0.0.1:11211"#本地memcache的地址端口
#         ]
#     }
# }
# CACHE_MIDDLEWARE_KEY_PREFIX = ''
# CACHE_MIDDLEWARE_SECONDS = 600
# CACHE_MIDDLEWARE_ALIAS = 'default'
#






LOGGING={
    'version':1,
    'disable_existing_logger':False,  #是否禁用之前的日志
    'handlers':{
        'file':{
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename':os.path.join(BASE_DIR,"django.log")
        }
    },
    'loggers':{
        'django':{
            'handlers':['file'],
            'level':'DEBUG',
            'propagate':True
        }
    }
}