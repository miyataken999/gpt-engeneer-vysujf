#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the Django development server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
