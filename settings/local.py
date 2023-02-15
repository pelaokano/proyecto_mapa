from .base import *
import pymysql
pymysql.install_as_MySQLdb()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# DATABASES = {
        # 'default': {
            # 'ENGINE': 'django.db.backends.mysql',
            # 'NAME': 'db_mysql_django',
            # 'USER': 'root',
            # 'PASSWORD': 'aalar009',
            # 'HOST': 'localhost',
            # 'PORT': '3306',
        # }
    # }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

