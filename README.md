# Too Many Daves
This repository contains the source code for the website, [toomanydaves.net](http://toomanydaves.net).

## System requirements for development
*   git
*   python/pip
*   mysql
*   [mysqlclient](https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-db-api-drivers)

## Set up a Dev database
Create a development database. Name it whatever you like.

    mysql -u root -p
    mysql> CREATE DATABASE toomanydaves_dev;

Create a user with a password and full access to the db.

    mysql> GRANT ALL PRIVILEGES ON toomanydaves_dev.* TO 'toomanydaves'@'localhost' IDENTIFIED BY 'dev';

Logging in to db with user to confirm success.

    mysql -u toomanydaves -p toomanydaves_dev

## Get and install the source
    git clone https://github.com/toomanydaves/toomanydaves.git
    cd toomanydaves
    pip3 install

## Create an .env file in the top-level directory to store your local credentials
    SECRET_KEY='+-v6=l%adqy7#hv5sff%^@=v-myynv0+47%#^^0f%nesx7a5m7'
    DEBUG=True
    DB_NAME='toomanydaves_dev'
    DB_USER='toomanydaves'
    DB_PASSWORD='dev'
    DB_HOST='localhost'
    DB_PORT=3306

## Migrate the db schema
    python3 manage.py migrate

## Add a superuser
    python3 manage.py createsuperuser

## Run the  server
    python3 manage.py runserver

## Make migrations
    python3 manage.py makemigrations

## Deploy to Production
