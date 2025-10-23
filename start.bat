@echo off
echo Starting SumanthCommerce...
echo.

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Running migrations...
python manage.py migrate

echo.
echo Populating sample data...
python manage.py populate_data

echo.
echo Starting development server...
echo Visit http://127.0.0.1:8000 in your browser
echo.
echo Default users:
echo - Admin: username=admin, password=admin123
echo - Customer: username=customer1, password=password123
echo.
python manage.py runserver
