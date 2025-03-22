from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-r!$ze+@gqt%q4#2ah^cd3soccv2k@oz1nzj1!j%)rnoub)qz2h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True


# Application definition

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',

    'rest_framework',
    'drf_yasg',

    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cbsg.urls'

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

WSGI_APPLICATION = 'cbsg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "CBSG Adminstration",
    "SITE_HEADER": "CBSG Adminstration",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    # "SITE_ICON": {
    #     "light": lambda request: static("icon-light.svg"),  # light mode
    #     "dark": lambda request: static("icon-dark.svg"),  # dark mode
    # },
    # # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    # "SITE_LOGO": {
    #     "light": lambda request: static("logo-light.svg"),  # light mode
    #     "dark": lambda request: static("logo-dark.svg"),  # dark mode
    # },
    # "SITE_SYMBOL": "speed",  # symbol from icon set
    # "SITE_FAVICONS": [
    #     {
    #         "rel": "icon",
    #         "sizes": "32x32",
    #         "type": "image/svg+xml",
    #         "href": lambda request: static("favicon.svg"),
    #     },
    # ],
    "SHOW_HISTORY": True, # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
    "THEME": "dark", # Force theme: "dark" or "light". Will disable theme switcher
    "STYLES": [
        lambda request: static("css/style.css"),
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),
    ],
    "BORDER_RADIUS": "6px",
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": False,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Home"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Company Profile"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/companyprofile",
                    },
                    {
                        "title": _("Home Banner"),
                        # "icon": "image",
                        "link": "/admin/core/homebanner",
                    },
                    {
                        "title": _("Recent Project"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/recentproject",
                    },
                    {
                        "title": _("Testimonial"),
                        # "icon": "",
                        "link": "/admin/core/testimonial",
                    },
                ],
            },
            {
                "title": _("About Us"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Core Competency"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/corecompetency",
                    },
                    {
                        "title": _("About"),
                        # "icon": "people",
                        "link": "/admin/core/about",
                    },
                    {
                        "title": _("Year Range"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/yearrange",
                    },
                    {
                        "title": _("History & Timeline"),
                        # "icon": "people",
                        "link": "/admin/core/historytimeline",
                    },
                    {
                        "title": _("Strategic Partners"),
                        # "icon": "people",
                        "link": "/admin/core/strategicpartner",
                    },
                ],
            },
            {
                "title": _("Our Service"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Service Intro"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/serviceintro",
                    },
                    {
                        "title": _("Sub Service Area"),
                        # "icon": "people",
                        "link": "/admin/core/subservicearea",
                    },
                    {
                        "title": _("Assignment"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/assignment",
                    },
                ],
            },
            {
                "title": _("Practice Area"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Practice Area"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/practicearea",
                    },
                ],
            },
            {
                "title": _("Our Team"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Team Member"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/teammember",
                    },
                ],
            },
            {
                "title": _("Our Work & Reach"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Milestone Work"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/milestonework",
                    },
                    {
                        "title": _("Work Location"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/worklocation",
                    },
                ],
            },
            {
                "title": _("Photo Gallery"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Photo Gallery"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/photogallery",
                    },
                ],
            },
            {
                "title": _("Contact"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Contact Details"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/contactdetail",
                    },
                ],
            },
            {
                "title": _("Report & Request"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Report"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/report",
                    },
                    {
                        "title": _("Request Form"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/requestform",
                    },
                ],
            },
            {
                "title": _("Blog"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Blog Manage"),
                        # "icon": "dashboard",  
                        "link": "/admin/core/blogpost",
                    },
                ],
            },
        ],
    },
}