#!/bin/bash
python blogpost/manage.py makemigrations
python blogpost/manage.py migrate
python blogpost/manage.py runserver 0.0.0.0:8000