#!/bin/sh

echo "Waiting for db..."
./wait-for-it.sh db:5432 --strict --timeout=30

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting server..."
exec gunicorn wallet_api.wsgi:application --bind 0.0.0.0:8000