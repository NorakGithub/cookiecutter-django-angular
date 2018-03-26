#!/bin/bash

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn --bind 0.0.0.0:8000 --timeout 6000 config.wsgi:application --log-level=INFO