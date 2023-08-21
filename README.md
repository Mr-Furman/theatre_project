# Theatre_project

Welcome to the Theatre documentation! This API is designed to organize work of theatre. 

## Features
* User registration and authentication
* Browse available theatre and their details
* Administer theatre and users

# Installation
Clone this repository

`git clone https://github.com/Mr-Furman/theatre_project`

Navigate to the project directory: 

`cd theatre_project`

Create and activate a virtual environment:

`python -m venv venv`

On Linux/Mac: `source venv/bin/activate`

On Windows: `venv\Scripts\activate`

Install the required packages: 

`pip install -r requirements.txt`

Run migrations: 

`python manage.py migrate`


Start the development server:

`python manage.py runserver`

# API Endpoints
## Authentication
POST /api/user/token/ - Obtain an access token using email and password (JWT 
authentication).
## Users
POST: /api/user/ - Register a new user
POST: /api/user/token/refresh/ - refresh JWT token
GET: /api/user/me/ - get my profile info
PUT/PATCH: user/me/ - update profile info 

## Theatre
GET: /api/theatre/ - get theatre info
GET: /api/theatre/genres/
GET: /api/theatre/actors/
GET: /api/theatre/theatre-halls/
POST: /api/theatre/genres/
POST: /api/theatre/actors/
POST: /api/theatre/theatre-halls/

# Contributing
We welcome contributions to enhance the functionality and usability of this API.

# License
This project is licensed under the MIT License. Feel free to use and modify the codebase as needed.
