# RestAPI_SpamGuard
This is a REST API that allows users to mark phone numbers as spam and search for names associated with phone numbers in the global database. The API is built using Django and Django REST framework, with a relational database for data persistence.

# Table of Contents
Features
Setup
API Endpoints
Data Population
Testing the API
Usage
Contributing

# Features
User registration with name, phone number, email address, and password.
Mark phone numbers as spam to share with other users via the global database.
Search for names associated with phone numbers in the global database.
View spam likelihood for each search result.
Automatic import of user's phone contacts into the app's database (not implemented in the API).

# Setup
To set up and run the API on your local machine, follow these steps:

1. Clone the repository to your local machine. <br>`git clone https://github.com/rajakamanishsingh/RestAPI_SpamGuard/`<br/>
2. Create a virtual environment and activate it (optional, but recommended).
3. Move Inside the Directory:<br>`cd RestAPI_SpamGuard`<br/>
4. Install the required dependencies using pip: <br>`pip install -r requirements.txt` <br/>
5. Apply database migrations:<br>`python manage.py migrate`<br/>
6. Create a superuser to access the Django admin interface:<br>`python manage.py createsuperuser`<br/>
7. Run the development server:<br>`python manage.py runserver`<br/>
8. Access the API at http://localhost:8000/api/.
API Endpoints
The API provides the following endpoints:

POST /mark_spam/: Mark a phone number as spam.
GET /search_by_name/<str:name_query>/: Search for names in the global database that match the given name query.
GET /search_by_phone_number/<str:phone_number>/: Search for names associated with the given phone number in the global database.
# Data Population
To test the API, you can use the included script or facility to populate the database with sample data. Run the following command:

<br>`python manage.py populate_data`<br/>
This will create random, sample data for testing the API.

# Testing the API
You can use tools like Postman or cURL to test the API endpoints. Make sure to include the required headers and request data as specified in each endpoint.

For example, to register a new user using cURL:

<br>`curl -X POST -H "Content-Type: application/json" -d '{
    "name": "John Doe",
    "phone_number": "1234567890",
    "email": "john@example.com",
    "password": "secretpassword"
}' http://localhost:8000/register_user/`<br/>

# Usage
This API is intended to be consumed by a mobile app or other frontend applications. The API provides endpoints for user registration, marking spam, and searching for names by phone number. It returns JSON responses that can be parsed and used by the frontend to display information to users.

Before using the API in a production environment, ensure that you have the required performance and security measures in place. Additionally, make sure to set up authentication and authorization to restrict access to certain endpoints as needed.

# Contributing
If you would like to contribute to this project, feel free to open issues or submit pull requests on the GitHub repository.
