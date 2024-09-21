#!/bin/sh

python manage.py makemigrations --noinput
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --access-logfile - --workers 4 --timeout 120 --reload \
  --bind app:8000 config.wsgi:application