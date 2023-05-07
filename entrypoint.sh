#!/bin/bash
cat /app/.env
python src/manage.py migrate
python src/manage.py runserver 0.0.0.0:8080

printenv
exec "$@"
