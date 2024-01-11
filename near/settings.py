from pathlib import Path
from environs import Env
from django.utils.timezone import timedelta

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("IS_DEVELOPMENT", False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", [])


INSTALLED_APPS = [
    "django.contrib.gis",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "tokens",
    "media",
    "users",
    "profiles",
    "emails",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "djangorestframework_camel_case.middleware.CamelCaseMiddleWare",
]

ROOT_URLCONF = "near.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "near.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

GDAL_LIBRARY_PATH = env("GDAL_LIBRARY_PATH")
GEOS_LIBRARY_PATH = env("GEOS_LIBRARY_PATH")

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = "static/"

MEDIA_URL = "files/"
MEDIA_ROOT = "files/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
        "profiles.permissions.HasProfileOrReadOnly",
        "users.permissions.IsEmailVerifiedOrReadOnly",
    ],
    "JSON_UNDERSCOREIZE": {
        "no_underscore_before_number": True,
    },
}

SIMPLE_JWT = {
    "UPDATE_LAST_LOGIN": True,
    "AUTH_HEADER_TYPES": ["Token", "Bearer"],
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
EMAIL_PORT = env.int("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = env("EMAIL_HOST_USER")
VERIFY_EMAIL_CODE_LIFETIME = timedelta(days=1)
