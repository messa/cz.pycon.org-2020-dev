#!/bin/bash

set -ex

python manage.py migrate

exec gunicorn -b 0.0.0.0:8000 --workers 4 --reload app
