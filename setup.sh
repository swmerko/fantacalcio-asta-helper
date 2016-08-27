#!/usr/bin/env bash
#encoding=utf8

git pull
virtualenv fantaEnv
echo
source fantaEnv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata auth
python manage.py loaddata players
echo "Installazione completata. Eseguire lo script di run!"