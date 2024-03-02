[![Django CI](https://github.com/Respect-J/TexnopromBack/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/Respect-J/TexnopromBack/actions/workflows/django.yml)
### Tehnoprom backend

Pre-requisites for local build:
__docker__ and __docker-compose__

-----------------------

Migrate the database:
`docker-compose run --rm backend python manage.py migrate`

Create your superuser:
`docker-compose run --rm backend python manage.py createsuperuser`

Run the server: `docker-compose up` and access on: _http://localhost:8000/admin_

-----------------------
In order to re-run:
`git pull` and `docker-compose up --build`
