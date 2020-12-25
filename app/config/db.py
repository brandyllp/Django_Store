import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'masteruser',
        'PASSWORD': 'Brandy1001',
        'HOST': 'database-2.cususk3yv9ie.us-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}
