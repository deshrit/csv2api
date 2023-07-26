#!/bin/env bash

set -e

python -m pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic --no-input

gunicorn -c gunicorn.conf.py
