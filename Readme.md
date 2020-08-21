# Add the project in Django
docker-compose run portfolio django-admin startproject personal_portfolio .

# Add new App(porfolio)  in Project
docker-compose run portfolio python manage.py startapp portfolio

# Add new App(blog)  in Project
docker-compose run portfolio python manage.py startapp blog

# Add new App in Project
docker-compose run portfolio python manage.py startapp 'app_name'

# Change Ownership of newly created App/Project
sudo chown -R $USER:$USER .

# create superUser
docker-compose run portfolio python manage.py createsuperuser
## input user,email, and pass

# change password of User
docker-compose run portfolio python manage.py changepassword <username>

# copy and rename sample-settings.py - settings.py
copy and rename personal_porfolio/sample-settings.py
to settings.py