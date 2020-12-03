web: gunicorn singing.wsgi
web: python manage.py collectstatic --noinput
release: python manage.py migrate