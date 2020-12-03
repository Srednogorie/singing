web: gunicorn singing.wsgi
heroku config:set DISABLE_COLLECTSTATIC=1
release: python manage.py migrate