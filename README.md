This is thew backend part of the Watering Schedule App.

## Getting started
First, clone or fork the repo (SSH). git clone `git@github.com:petmetic/watering_schedule_backend.git`
Navigate to backend folder. Install the virtual environment: `python3.11 -m venv venv`

Activate the virtual environment: `. venv/bin/activate`

In the project folder of the application, install the requirements

`pip install -r requirements.txt`


Create database: go to the `src` folder in project and run

`./manage.py migrate`

Create admin superuser for Admin view. Run command and follow the prompts:

`./manage.py createsuperuser`


## How to run application
To run the application locally, in your `src` folder, enter in terminal:

`./manage.py runserver`

Go to http://127.0.0.1:8000 to see the site.