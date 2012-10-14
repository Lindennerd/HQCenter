#encoding: utf-8

import os
ROOTPATH = os.path.dirname(__file__)
AUTH_PROFILE_MODULE = 'userinfo.User'


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Luiz Paulo', 'luizpaulo_l@hotmail.com'),
	('Luiz Paulo', 'luizpaulo_l@hotmail.com'),
	('Luiz Paulo', 'luizpaulo_l@hotmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'HQCenter',                      
        'USER': 'root',                      
        'PASSWORD': '574rw4r5',                  
        'HOST': '',                      
        'PORT': '',                      
    }
}

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(ROOTPATH, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(ROOTPATH, 'static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
	os.path.join(ROOTPATH, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)
SECRET_KEY = 'e=crbc676rogxli#ky2y&amp;-@12%kst(p2(2@8j%@i=jc8@)9obg'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', 
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'HQCenter.urls'


WSGI_APPLICATION = 'HQCenter.wsgi.application'

TEMPLATE_DIRS = (
	os.path.join(ROOTPATH, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.comments',

	'core',
	'accounts',
    'south',
    'debug_toolbar',
    'userinfo',    
)

INTERNAL_IPS = ('127.0.0.1')

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
