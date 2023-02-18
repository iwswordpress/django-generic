### VENV

python -m venv venv

THIS WORKS

- Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

- Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

python -m ensurepip -U

.\venv\Scripts\activate

### DJANGO

default_auto_field = 'django.db.models.BigAutoField'

pip install django

pip freeze > requirements.txt

in venv

- python -m pip freeze > requirements.txt

- python -m pip install -r requirements.txt

django-admin startproject core .

https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata

./manage.py dumpdata > db.json

dumpdata for backup specific app

./manage.py dumpdata app > app.json

### GIT

git rm -r --cached .

git remote remove origin

git remote add origin https://github.com/iwswordpress/drl-python-test.git
