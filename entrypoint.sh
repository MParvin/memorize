#!/bin/bash

python manage.py makemigrations

python manage.py migrate

gunicorn --bind :8001 memorize.wsgi:application