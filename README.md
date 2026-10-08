# WhatBytes Healthcare Backend

A secure healthcare backend API built using Django, Django REST Framework, PostgreSQL, and JWT authentication.

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT
- Django ORM
- PostgreSQL Driver
- python-dotenv

## Features

- User registration
- JWT authentication
- User login
- Patient CRUD
- Doctor CRUD
- Patient-doctor mapping
- Authentication and authorization
- Patient ownership protection
- Request validation
- Duplicate mapping prevention
- PostgreSQL database
- Django Admin

## Project Structure

```text
whatbytes-healthcare-backend/
│
├── accounts/
├── patients/
├── doctors/
├── mappings/
├── config/
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd whatbytes-healthcare-backend
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file using `.env.example` as a reference.

### 5. Configure PostgreSQL

Create a PostgreSQL database and configure the database credentials in `.env`.

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create admin user

```bash
python manage.py createsuperuser
```

### 8. Start the server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Authentication

```text
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/token/refresh/
```

### Patients

```text
POST   /api/patients/
GET    /api/patients/
GET    /api/patients/<id>/
PUT    /api/patients/<id>/
DELETE /api/patients/<id>/
```

### Doctors

```text
POST   /api/doctors/
GET    /api/doctors/
GET    /api/doctors/<id>/
PUT    /api/doctors/<id>/
DELETE /api/doctors/<id>/
```

### Patient-Doctor Mappings

```text
POST   /api/mappings/
GET    /api/mappings/
GET    /api/mappings/patient/<patient_id>/
DELETE /api/mappings/<id>/
```

## Authentication

Protected endpoints require a JWT access token.

Use the following HTTP header:

```text
Authorization: Bearer <access_token>
```

## Security

- Passwords are securely hashed using Django's password hashing system.
- JWT authentication is used for API authentication.
- Patient records are restricted to their creator.
- Duplicate patient-doctor mappings are prevented.
- Sensitive configuration is stored using environment variables.

## Database

PostgreSQL is used as the application's relational database and Django ORM is used for database operations.

## Testing

The APIs can be tested using Postman or another REST API client.

## Author

Developed as part of the WhatBytes Full Stack Intern assignment.