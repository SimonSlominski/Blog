# About

This is a demo project for practicing Django. The idea was to build some basic blogging platform.

The application was created using **Python 3.7** and **Django 1.8** and **SQLite** database. While creating the application, the inspiration was the book  _**“Two Scoops of Django. Best practices for Django 1.8”**_, hence the choice of the Django version.

## Features

### Current features include:
-	CRUD operations with class-based views
-	Slug-only urls to improve SEO
-	Pagination
-	Sharing posts via e-mail
-	Comments
-	Tags
-	RSS feeds
-	Sitemap

### Dependencies
-	Django
-	django-taggit
-	django-taggit-serializer
-	EditorConfig
-	Markdown
-	Pytz

# Setup

### Prerequisites
**[Optional] Install virtual environment:**

$ python3 -m venv env


**[Optional] Activate virtual environment:**

On macOS and Linux:

$ source env/bin/activate


### Install dependencies:
$ pip install -r requirements.txt

### Set Database
python manage.py makemigrations

python manage.py migrate

### Create SuperUser
python manage.py createsuperuser

