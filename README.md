# 📌 Django REST API for App Management

## 🚀 Overview
This is a **Django REST Framework (DRF) API** that allows users to **add, retrieve, and delete applications**.  
It provides a structured way to manage application details such as name, version, and description.

---

## 🛠 Installation and Setup
Follow these steps to set up and run the project locally.

1. Clone the Repository
   git clone https://github.com/your-username/your-repo.git

   cd your-repo

3. Create and Activate a Virtual Environment
   
   For Windows (cmd or PowerShell):

   python -m venv venv

   venv\Scripts\activate


5. Apply Database Migrations

   python manage.py migrate

4. Run the Development Server

   python manage.py runserver

The API should now be running at http://127.0.0.1:8000/

## API Endpoints

| Method  | Endpoint               | Description            |
|---------|------------------------|------------------------|
| `POST`  | `/api/add-app/`        | Add a new app          |
| `GET`   | `/api/get-app/{id}/`   | Get app by ID         |
| `DELETE`| `/api/delete-app/{id}/` | Delete app by ID      |


## Usage & Testing the API

Using Postman

   Open Postman

   Set the method to POST, GET, or DELETE

   Enter the API URL (e.g., http://127.0.0.1:8000/api/add-app/)

   Go to the Body tab, select raw, and choose JSON format

Enter request data:

{

    "name": "Sample App",
    
    "version": "1.0.0",
    
    "description": "This is a sample application."
    
}

Click Send to test the API


Task 2: Database Management 

To test your Task 2 API (which interacts with the SQLite or PostgreSQL database and performs CRUD operations), follow these steps to ensure the endpoints are working correctly:

1. Test the GET API to fetch all apps
This API endpoint should return a list of all apps stored in the database.

Using Postman:
HTTP Method: GET

URL: http://127.0.0.1:8000/api/get-apps/

Expected Response:

[
    {
        "id": 1,
        "name": "Test App",
        "version": "1.0.0",
        "description": "This is a sample test app."
    },
    {
        "id": 2,
        "name": "Another App",
        "version": "2.1.0",
        "description": "Another test application."
    },
    {
        "id": 3,
        "name": "New App",
        "version": "1.0.1",
        "description": "This is a newly added app."
    }
]

2. Test the POST API to create a new app

This API endpoint should allow you to add a new app to the database.

Using Postman:
HTTP Method: POST

URL: http://127.0.0.1:8000/api/add-app/

Body (JSON format):


]
{
    "name": "Sample App",
    "version": "1.0.0",
    "description": "A sample app description."
}
Expected Response:
json
Copy
Edit
{
    "id": 4,
    "name": "Sample App",
    "version": "1.0.0",
    "description": "A sample app description."
}
This response should indicate that the app was successfully added to the database.

3. Test the GET API again
After adding a new app, you should test the GET API again to ensure the newly added app appears in the list.

HTTP Method: GET

URL: http://127.0.0.1:8000/api/get-apps/

Expected Response (including the newly added app):


[
    {
        "id": 1,
        "name": "Test App",
        "version": "1.0.0",
        "description": "This is a sample test app."
    },
    {
        "id": 2,
        "name": "Another App",
        "version": "2.1.0",
        "description": "Another test application."
    },
    {
        "id": 3,
        "name": "New App",
        "version": "1.0.1",
        "description": "This is a newly added app."
    },
    {
        "id": 4,
        "name": "Sample App",
        "version": "1.0.0",
        "description": "A sample app description."
    }
]

