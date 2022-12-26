# MyShopperSite API

## Development Interview Round

The aim of this project is to build a simple REST API using Django framework.

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/praty-1698/MyShopperSite.git
    $ cd myshoppersite
    
Activate the virtualenv for your project.

    $ source <environment_directory>/bin/activate
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

[Link to development log](https://docs.google.com/document/d/1NJvoInKN770gSGlecXWeYf5bwE6KfLJtdPetOdZpKEk/edit#)

## How to use this API?

Use the following to view, create and update `Customer` name and phone number:

View all recent customer entries:

    $ http://127.0.0.1:8000/customer_list/

View specific customer entry:

    $ http://127.0.0.1:8000/customer_detail/<customer_id>/

Create customer entry:

    $ http://127.0.0.1:8000/create_customer/

Update customer entry:

    $ http://127.0.0.1:8000/cupdate_customer/<customer_id>/
