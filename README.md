# install django
pip install Django==1.9.13

# set python interpreter
CocCommand python.setInterpreter

# git use store credential
git config --global credential.helper store

# create project
django-admin startproject myproject

# run server
python manage.py runserver 0.0.0.0:80

# start app
python manage.py startapp myapp

# migrate
python manage.py migrate

# create superuser
python manage.py createsuperuser

# user aziz

