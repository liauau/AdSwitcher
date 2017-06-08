rm -rf db.sqlite3 ./switcher/migrations/*
touch switcher/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  --username testAuth --email liauau2009@qq.com


