# Neigborhood
A python application based on Django framework, 

### 25/10/2019

## By **[Daniel Njuguna](https://github.com/dan-jugz/hoodie)**

## Description

This is an application that enables a authenticated user to post events for other neighbours to see. A user can click on an a user to view their pages and can also view a list of businesses in the area also can also have access to emergency contacts.

## User Stories
As a user I would like to:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Behavior Driven Development

| Behaviour    | Input     | Output|
| :------------- | :------------- |:---------|
|   View all post from database    |    Post is saved in a database | Post from database|
|View user page|Click on a user name|Display users page|
|View emergency contacts |Click emergency button |Display emergency contact  details|


## Setup/Installation Requirements

* `$ git clone` [hood](https://github.com/dan-jugz/hoodie)
* `$ cd hood`


    ```python
    #create a .env file
    SECRET_KEY = '<Secret_key>'
    DBNAME = 'hood'
    USER = '<username>'
    PASSWORD = '<password>'
    DEBUG = True

    ```    

* `$ python3.6 -m venv virtual` to create a  virtual environment
* `$ source virtual/bin/activate` to activate the virtual environment
* `$ psql` to activate the postgres server
* `$ username=create database pixels` create db with the name hood2
* run `$ python3.6 -m pip install -r requirements.txt ` to install dependencies
* `$ python3.6 manage.py makemigrations` to initialize database migrations
* `$ python3.6 manage.py migrate` to commit the migration you are running
* `$ python3.6 manage.py runserver` to run the app
* open `localhost:8000` to view the app

## Known Bugs
* none.

### Support and contact details 
* you can contact me on **njugunadaniel364@gmail.com**

## Technologies Used

* Python3.6
* Django 1.11
* Bootstrap
* WhiteNoise
* PostgreSQL Database
* CSS


### License

MIT (c) 2019 **[Daniel Njuguna](https://github.com/dan-jugz/hoodie)**