# Dependencies:

## Django

```bash: pip install Django```

## Psycopg2

```bach: pip install psycopg2-binary```

# Configure Database:

Go to path `./blog/setting.py` and modify DATABASES environment like this:

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

1. execute command in shell or bash: ```bash: git clone https://github.com/K1000o-Lp/django-blog.git```
2. execute command in app directory shell: ```bash: python manage.py makemigrations blog_app```
3. execute command: ```bash: python manage.py runserver```