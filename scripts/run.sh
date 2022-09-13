#!/usr/bin/env bash

echo "Starting server"

python manage.py collectstatic --no-input --clear
python manage.py migrate

gunicorn -w $((2 * $(nproc) + 1 )) \
  -b 0.0.0.0:$PORT \
  --log-level=error \
  wsgi:application

exec "$@"