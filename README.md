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
