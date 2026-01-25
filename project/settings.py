from datetime import timedelta
from pathlib import Path
from decouple import config
import os

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _



BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-)f7+=ng1#%pgoww+%!9przfpc7^!m86fs!o@i1hq0(z2f2gnx4'

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [

    # unfold package apps

    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    "unfold.contrib.location_field",  # optional, if django-location-field package is used
    "unfold.contrib.constance",

    # default django apps

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',

    # Local apps
    'apps.user',
    'apps.services',
    'apps.order_management',
    'apps.product',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),   
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),      
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'
AUTH_USER_MODEL = 'user.CustomUser'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# import stripe credential from .env
STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY')

STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY') 

STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET')



UNFOLD = {
    
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "command_search": True,  # Replace the sidebar search with the command search
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("User Management"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                   
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:user_customuser_changelist"),
                    },
                    {
                        "title": _("Vendor Profiles"),
                        "icon": "store",
                        "link": reverse_lazy("admin:user_vendorprofile_changelist"),
                    },
                    
                ],
            },
             {
                "title": _("Product Management"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                   
                    {
                        "title": _("Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:product_productcategory_changelist"),
                    },
                    {
                        "title": _(" Products"),
                        "icon": "store",
                        "link": reverse_lazy("admin:product_product_changelist"),
                    },
                    
                ],
            },
            {
                "title": _("Order Management"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                   
                    {
                        "title": _("RepairOrders"),
                        "icon": "orders",
                        "link": reverse_lazy("admin:order_management_repairorder_changelist"),
                    },
                   
                    
                ],
            },
        ],
    },
   
}



