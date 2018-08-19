# ISA website

This is an attempt to migrate the existing ISA website (built using a custom PHP backend to Wagtail). The aim is produce a site that is easier to maintain and handover.
The flexiblity of Wagtail should allow for bespoke integrations to be achieved where required. 


So far this repo contains a vanilla install of the latest version of wagtail (2.2.1 at the time of writing)
I have added the necessary code for Heroku deployment.

To get started:

1. set up a virtualenv
2. clone the repo: git clone git@github.com:timcknowles/isa_website.git
3. CD into isa_website
3. Run the following

Install the requirments:
pip install -r requirements.txt

Create a local postrgres DB:

createdb isa_website

Run the migrations and create a superuser:

./manage.py migrate
./manage.py createsuperuser

Check it runs locally

./manage.py runserver

To make git push heroku master work - follow the steps in this guide most of which has been done already for you:

https://wagtail.io/blog/wagtail-heroku-2017/

NB: you will need to load your own ENV variables locally (for the Django secret key) and into a .env file for heroku (see guide).  The Django secret key will have to be generated manually as this step is usaully done by the wagtail start command.
