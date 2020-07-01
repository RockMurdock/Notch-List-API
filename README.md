# Notch-List RESTful API 

This is the back-end counterpart to the full-stack [Notch-List Web App](https://github.com/RockMurdock/Notch-List). A full description of the app can be found there. 

# Project Setup

1. Clone the repo and cd into it:

    `git@github.com:RockMurdock/Notch-List-API.git`

1. Set up your virtual environment:

    `python -m venv notchlistEnv`

1. Activate virtual environment:

    `source ./notchlistEnv/bin/activate`

1. Install dependencies:

    `pip install -r requirements.txt`

1. Run migrations:

    `python manage.py makemigrations`
    `python manage.py migrate`

1. Load fixtures:

    `python manage.py loaddata glasswares.json`
    `python manage.py loaddata drink_styles.json`


1. Start the API server:

    `python manage.py runserver`

1. Follow the [steps on the front-end web app readme](https://github.com/RockMurdock/Notch-List) to view the web app in your browser

## Technology Utilized
1. Django
1. Python
1. SQLite
1. Fixtures
1. ORM
1. Models
1. API Endpoint Views  
1. User authentication with authtoken
1. Url Routing

## Entity Relationship Diagram
![ERD](notchlist/ERD/Notch List (3).png)
