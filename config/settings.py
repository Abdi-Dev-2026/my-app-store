import os
from pathlib import Path

# 1️⃣ Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 2️⃣ Security Settings
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')
DEBUG = False
ALLOWED_HOSTS = ['*']

# 3️⃣ CSRF Trusted Origins (Production)
CSRF_TRUSTED_ORIGINS = [
    "https://my-app-store-production.up.railway.app",
]

# 4️⃣ Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'cloudinary_storage',         # Cloudinary static & media
    'django.contrib.staticfiles',

    'cloudinary',                 # Cloudinary API

    'store',                      # Your main app
    'accounts',                   # Accounts / auth app
]

# 5️⃣ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # Static file serving

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',    # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'store.middleware.MaintenanceModeMiddleware',   # Optional maintenance mode
]

# 6️⃣ URL Configuration
ROOT_URLCONF = 'config.urls'

# 7️⃣ Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# 8️⃣ WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# 9️⃣ Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 10️⃣ Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 11️⃣ Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 12️⃣ Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticCloudinaryStorage'  # Production-ready

# 13️⃣ Cloudinary Media Storage
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('API_KEY'),
    'API_SECRET': os.environ.get('API_SECRET'),
}

# 14️⃣ Media (Optional fallback, mostly Cloudinary used)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 15️⃣ Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 16️⃣ Login / Logout redirects
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'