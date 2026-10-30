#!/bin/sh
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn movietrack.wsgi:application \
    --bind 127.0.0.1:8000 \
    --workers 2 \
    --access-logfile - \
    --error-logfile - &

exec nginx -g "daemon off;"