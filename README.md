# Too Many Daves
This repository contains the source code for the website, [toomanydaves.net](http://toomanydaves.net).

## System requirements for development
*   git
*   python/pip
*   mysql
*   [mysqlclient](https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-db-api-drivers)

## Set up the Dev database
Create a development database called _toomanydaves-dev_.

    mysql -u root -p
    mysql> CREATE DATABASE toomanydaves-dev;

Create a user called _toomanydaves_ with password _dev-password_ and full access to the db.

    mysql> GRANT ALL PRIVILEGES ON toomanydaves-dev.* TO 'toomanydaves'@'localhost'
        -> IDENTIFIED BY 'dev-password';

## Get and install the source
    git clone https://github.com/toomanydaves/toomanydaves.git
    cd toomanydaves
    pip3 install
    python3 manage.py migrate

## Run the Dev server
    python3 manage.py runserver

## Deploy to Production
