[![Django CI](https://github.com/Respect-J/TexnopromBack/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/Respect-J/TexnopromBack/actions/workflows/django.yml)

ЗАПУСК BACK_END ТЕХНОПРОМ



MAC os:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser (дальше нужно следовать инструкциям и создать админа)
python3 manage.py runserver


Windows os:
python -m venv venv
venv/Scripts/activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser (дальше нужно следовать инструкциям и создать админа)
python manage.py runserver
