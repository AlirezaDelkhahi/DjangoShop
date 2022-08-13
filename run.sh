#!bin/bash

python manage.py makemigrations core customer order product api
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

