#!/usr/bin/env bash
#encoding=utf8

source fantaEnv/bin/activate
python manage.py runserver
echo "Ora aprire il browser all'indirizzo: http://localhost:8000"