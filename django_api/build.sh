#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

cd .. python manage.py collectstatic --no-input
cd .. python manage.py migrate