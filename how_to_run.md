
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

<br>POST /mark_spam/: Mark a phone number as spam.<br/>
<br>GET /search_by_name/<str:name_query>/: Search for names in the global database that match the given name query..<br/>
<br>GET /search_by_phone_number/<str:phone_number>/: Search for names associated with the given phone number in the global database..<br/>
# Data Population
To test the API, you can use the included script or facility to populate the database with sample data. Run the following command:

<br>`python manage.py populate_data`<br/>
This will create random, sample data for testing the API.

# Testing the API
You can use tools like Postman or cURL to test the API endpoints. Make sure to include the required headers and request data as specified in each endpoint.

<br>`curl http://localhost:8000/search_by_name/John/`<br/>

<br>`curl http://localhost:8000/search_by_phone_number/1234567890/`<br/>

<br>`curl http://localhost:8000/mark_spam/1234567890/`<br/>
