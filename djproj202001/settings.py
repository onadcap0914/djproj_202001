"""
Django settings for djproj202001 project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
"""
[1] onad | 20200323 | Activate Python Django Admin Interface
[2] onad | 20200323 | Create x_base_bootstrap_hdr_ftr.html template (initial draft)
[5] onad | 20200330 | Application login functionality
[6] onad | 20200330 | Application Logout functionality
[8] onad | 20200331 | Password reset functionality
[9] onad | 20200401 | Protected/secured views
[10] onad | 20200401 | Bootstrap4 and crispy forms
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#b1beb09=_en$oe8%_p1^^3n2kmkayzjb59@0w4)4sx7_&@soy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '192.168.0.14', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',     #[1]
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',     #[10]
    'djproj202001',
]

#[10]
#Django crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djproj202001.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', 'membership/templates',
                 'accounting/templates', 'transaction/templates',
                 'system_setting/templates', 'report/templates', ],     #[2]
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

WSGI_APPLICATION = 'djproj202001.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = BASE_DIR      #[2]
STATIC_URL = '/static/'

#[2]
# Additional locations of static files
STATICFILES_DIRS = (
	('assets', os.path.join(BASE_DIR, 'static/')),
)

#[5] [9]
LOGIN_REDIRECT_URL = 'logged_in'

#[6]
LOGOUT_REDIRECT_URL = 'site_home'

#[8]
#Simulate email backend, add this line in the settings.py.
#Comment out this line in the prod environment
#>python manage.py sendtestemail test_user01@example.com
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

