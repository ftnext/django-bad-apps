#!/usr/bin/env bash
set -euo pipefail

echo "Apply database migrations"
python manage.py migrate
echo

echo "Start server"
python manage.py runserver 0.0.0.0:8000
