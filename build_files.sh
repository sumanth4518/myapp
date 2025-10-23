pip install -r requirements.txt
python manage.py collectstatic
python manage.py runserver 0.0.0.0:${PORT:-8000}
