# django-bakery V0.2.1.0
Django ecommerce app for a local bakery.
## General info
This is a Django app for a local bakery to sell it's desserts online. One can buy desserts on it's online store or contact a local store for a special request.
## Technologies
- python 3.9
- pipenv 2020.11.15
- django 3.1.7
- fontawesome-free 5.15.2
- gunicorn 20.0.4
- whitenoise 5.2.0
- pillow 8.1.2
## Setup
1. Download the source code.
2. Install the proyect dependencies 
```
pipenv install
```
3. Apply the model migrations
```
pipenv run ./manage.py makemigrations
pipenv run ./manage.py migrate
```
4. Create a superuser for the admin site
```
pipenv run ./manage.py createsuperuser
```
n. Start the server in the virtual environment's context.
```
pipenv run ./manage.py runserver
```
### Example deploys

- [Heroku](https://django-bakery.herokuapp.com/)

## Status
This version corresponds to an assignment from FullStack II:

***Create a Django Project with at least 2 models (3 fields each) that serves 2 static images and media images.***

### Notes
- Django doesn't support serving files on deploy, it's advised to use a separate server for it. This means the server must run on *debug mode* to be able to serve files.
- On one of the ListViews, there are links for dynamic pages (details for each product) but it's currently without any functionality.
- To deploy the site on Heroku, another database engine must be used instead of sqlite. Since Heroku provides a free PostgreSQL database, that's what will be used.

### TODO
- [x] Catalog page.
- [ ] Refactor the css stylesheet into a group of SCSS files.
- [ ] Refactor the design to be responsive.
- [ ] Move the static files to a CDN.
- [ ] Serve dynamic pages.
- [x] Use a database to store data.
- [x] Admin page.
- [x] Serve media files stored in the data models.
- [ ] Shopping cart.
- [ ] Carousel for sales on the homepage.
- [ ] Deploy the app with debug mode off.