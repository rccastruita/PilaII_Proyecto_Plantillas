# Laura's Bakery
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
## Setup
1. Download the source code.
2. Install the proyect dependencies with. 
```
pipenv install
```
3. Start the server in the virtual environment's context.
```
pipenv run ./manage.py runserver
```
### Example deploys

- [Heroku](https://lit-cliffs-17781.herokuapp.com/)
## Status
Currently, this is just a static website rendered with Django templates. It uses a static css file to give style to the templates, in the future this will be done with a SCSS engine.
### TODO
- [ ] Catalog page.
- [ ] Refactor the css style into a group of SCSS files.
- [ ] Move the static files to a CDN.
- [ ] Serve dynamic pages.
- [ ] Use a database to store data.
- [ ] Admin page.