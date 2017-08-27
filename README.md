# Too Many Daves
This repository contains the source code for the website, [toomanydaves.net](http://toomanydaves.net).

## System requirements for development
*   git
*   python/pip
*   mysql

## Set up the Dev database
Create a database called _toomanydaves_.

    mysql -u root -p
    mysql> CREATE DATABASE toomanydaves;

Create a user called _toomanydaves-admin_ with password _dev-password_ and full access to the db.

    mysql> GRANT ALL PRIVILEGES ON toomanydaves.* TO 'toomanydaves-admin'@'localhost'
        -> IDENTIFIED BY 'dev-password';

## Get and install the source
    git clone https://github.com/toomanydaves/toomanydaves.git
    cd toomanydaves
    pip3 install
    python3 manage.py migrate

## Run the Dev server
    python3 manage.py runserver

## Deploy to Production
