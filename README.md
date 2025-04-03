# django-project

Introduction
This is a simple Django REST API that allows users to manage applications. The API provides endpoints to add, retrieve, and delete applications.

Prerequisites
Ensure you have the following installed on your system before proceeding:
Python 3.8+
Django 4+
Django REST Framework
PostgreSQL or SQLite (default)

Installation and Setup
1. Clone the Repository
Open a terminal or command prompt and run:
git clone https://github.com/yourusername/your-repo.git
cd your-repo

2. Create and Activate a Virtual Environment
For Windows (cmd or PowerShell):
python -m venv venv
venv\Scripts\activate

3. Apply Database Migrations
python manage.py migrate

5. Run the Development Server
python manage.py runserver

The API should now be running at http://127.0.0.1:8000/

## API Endpoints
| Method  | Endpoint               | Description            |
|---------|------------------------|------------------------|
| `POST`  | `/api/add-app/`        | Add a new app          |
| `GET`   | `/api/get-app/{id}/`   | Get app by ID         |
| `DELETE`| `/api/delete-app/{id}/` | Delete app by ID      |


Usage & Testing the API
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
