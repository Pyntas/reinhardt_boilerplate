#!/usr/bin/env bash

#Give me permissions :) chmod +x syncdb.sh to execute me.

USERNAME="admin"
EMAIL="admin@email.com"

echo "Use just for local development or testing with SQLite3"

rm ../db.sqlite3
python manage.py syncdb --noinput
echo "Setting up super user, please set a PASSWORD"

python manage.py createsuperuser --username=$USERNAME --email=$EMAIL
