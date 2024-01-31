# Dependencies:

## Django

```pip install Django```

## Psycopg2

```pip install psycopg2-binary```

# Configure Database:

Go to path './blog/setting.py' and modify DATABASES environment like this:

```python:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB_NAME',
        'USER': 'USER_DB',
        'PASSWORD': 'PASSWORD_DB',
        'HOST': 'localhost',
        'PORT': '5432',
    }
```

# Installation:

1. execute command in shell or bash: ```git clone https://github.com/K1000o-Lp/django-blog.git```
2. execute command in app directory shell: ```python manage.py makemigrations blog_app```
3. execute command: ```python manage.py runserver```