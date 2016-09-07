#!/bin/sh

#echo "---- Migrations ----"
#python manage.py makemigrations
#python manage.py migrate

echo "---- Default Admin ----"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@therapyapp.local', 'nahibatayenge')" | python manage.py shell

#echo "---- Load Initial data ----"
#python manage.py loaddata main/fixtures/initial_folder_data.json
#python manage.py loaddata main/fixtures/stable_1.0.json