#!/bin/bash
python src/manage.py migrate
python src/manage.py runserver 8000:8000