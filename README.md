# WhatBytes Healthcare Backend

A secure healthcare backend API built using **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT authentication**.

This project was developed as part of the **WhatBytes Full Stack Intern Assignment – Django Healthcare Backend**.

The backend provides APIs for:

- User registration and authentication
- JWT-based authentication
- Patient management
- Doctor management
- Patient-doctor mappings
- Input validation and error handling
- Authorization and ownership controls
- PostgreSQL database integration
- Automated API testing

---

## Tech Stack

- **Python 3**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Django ORM**
- **djangorestframework-simplejwt**
- **python-dotenv**
- **django-cors-headers**
- **psycopg2-binary**

---

## Features

### Authentication

- User registration
- User login
- JWT access and refresh tokens
- Custom user model
- Email-based authentication
- Password hashing using Django
- Protected API endpoints
- Session authentication for the Django REST Framework browsable API

### Patient Management

Authenticated users can:

- Create patients
- View their own patients
- View individual patients
- Update patients
- Delete patients

Each patient is associated with the user who created the patient.

Users cannot access or modify patients belonging to another user.

### Doctor Management

Authenticated users can:

- Create doctors
- View doctors
- View individual doctors
- Update doctors
- Delete doctors

### Patient-Doctor Mapping

Authenticated users can:

- Assign doctors to patients
- View patient-doctor mappings
- View doctors assigned to a specific patient
- Remove doctor assignments
- Prevent duplicate patient-doctor assignments

Users can only create and delete mappings involving patients they own.

### Validation

The API validates:

- Required fields
- Email format
- Duplicate email addresses
- Password length
- Patient ownership
- Doctor/patient relationships
- Duplicate mappings
- Phone number format

---

# Project Structure

```text
whatbytes-healthcare-backend/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── managers.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── patients/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── doctors/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── mappings/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# Database Design

The application uses **PostgreSQL** as its database.

## User

The custom user model contains:

- ID
- Name
- Email
- Phone
- Password
- Active status
- Staff status
- Creation timestamp

Email is used as the unique login identifier.

## Patient

Each patient contains:

- ID
- Name
- Email
- Phone
- Date of birth
- Address
- Created by
- Created timestamp
- Updated timestamp

Each patient belongs to the user who created it.

## Doctor

Each doctor contains:

- ID
- Name
- Specialization
- Email
- Phone
- Created timestamp
- Updated timestamp

## PatientDoctorMapping

The mapping table connects patients and doctors.

Each mapping contains:

- ID
- Patient
- Doctor
- Assignment timestamp

A unique database constraint prevents the same doctor from being assigned to the same patient more than once.

---

# Authentication

The API uses JWT authentication through:

```text
djangorestframework-simplejwt
```

After successful login, the API returns an access token and refresh token.

Example:

```json
{
    "message": "Login successful.",
    "access": "ACCESS_TOKEN",
    "refresh": "REFRESH_TOKEN",
    "user": {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }
}
```

For protected API requests, include the access token in the request header:

```text
Authorization: Bearer <access_token>
```

---

# Environment Variables

Sensitive configuration is stored using environment variables.

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=django-insecure-change-this-secret-key
DEBUG=True

DB_NAME=whatbytes_healthcare
DB_USER=healthcare_user
DB_PASSWORD=healthcare_password
DB_HOST=localhost
DB_PORT=5432

JWT_ACCESS_TOKEN_MINUTES=60
JWT_REFRESH_TOKEN_DAYS=7
```

> Do not commit the real `.env` file to GitHub.

The `.env` file is excluded through `.gitignore`.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/AntonyJohny/whatbytes-healthcare-backend.git
```

Move into the project directory:

```bash
cd whatbytes-healthcare-backend
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Make sure PostgreSQL is installed and running.

Create the database:

```sql
CREATE DATABASE whatbytes_healthcare;
```

Create the database user:

```sql
CREATE USER healthcare_user WITH PASSWORD 'healthcare_password';
```

Grant database permissions:

```sql
GRANT ALL PRIVILEGES ON DATABASE whatbytes_healthcare TO healthcare_user;
```

Connect to the database:

```sql
\c whatbytes_healthcare
```

Grant schema permissions:

```sql
GRANT ALL ON SCHEMA public TO healthcare_user;
```

The automated Django test suite creates a temporary test database, so the PostgreSQL user should also have permission to create databases:

```sql
ALTER USER healthcare_user CREATEDB;
```

---

# Configure Environment

Create a `.env` file in the project root:

```text
.env
```

Example:

```env
SECRET_KEY=django-insecure-change-this-secret-key
DEBUG=True

DB_NAME=whatbytes_healthcare
DB_USER=healthcare_user
DB_PASSWORD=healthcare_password
DB_HOST=localhost
DB_PORT=5432

JWT_ACCESS_TOKEN_MINUTES=60
JWT_REFRESH_TOKEN_DAYS=7
```

---

# Run Migrations

Create migrations if required:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

# Create Superuser

To access Django Admin:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

---

# Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# API Endpoints

All endpoints except registration and login require authentication.

---

# Authentication APIs

## Register User

```text
POST /api/auth/register/
```

Request:

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123",
    "phone": "9876543210"
}
```

Response:

```json
{
    "message": "User registered successfully.",
    "user": {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "9876543210"
    }
}
```

---

## Login

```text
POST /api/auth/login/
```

Request:

```json
{
    "email": "john@example.com",
    "password": "password123"
}
```

Response:

```json
{
    "message": "Login successful.",
    "access": "ACCESS_TOKEN",
    "refresh": "REFRESH_TOKEN",
    "user": {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }
}
```

---

## Refresh Access Token

```text
POST /api/auth/token/refresh/
```

Request:

```json
{
    "refresh": "REFRESH_TOKEN"
}
```

Response:

```json
{
    "access": "NEW_ACCESS_TOKEN"
}
```

---

# Patient APIs

## Create Patient

```text
POST /api/patients/
```

Authentication:

```text
Authorization: Bearer <access_token>
```

Request:

```json
{
    "name": "Alice Smith",
    "email": "alice@example.com",
    "phone": "9876543210",
    "date_of_birth": "1995-06-15",
    "address": "Bengaluru, Karnataka"
}
```

---

## List Patients

```text
GET /api/patients/
```

Returns patients created by the authenticated user.

---

## Get Patient

```text
GET /api/patients/<id>/
```

Example:

```text
GET /api/patients/1/
```

---

## Update Patient

```text
PUT /api/patients/<id>/
```

Example:

```text
PUT /api/patients/1/
```

Request:

```json
{
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "phone": "9876543210",
    "date_of_birth": "1995-06-15",
    "address": "Bengaluru, Karnataka"
}
```

---

## Delete Patient

```text
DELETE /api/patients/<id>/
```

Example:

```text
DELETE /api/patients/1/
```

---

# Doctor APIs

## Create Doctor

```text
POST /api/doctors/
```

Request:

```json
{
    "name": "Dr. Smith",
    "specialization": "Cardiology",
    "email": "smith@example.com",
    "phone": "9876543210"
}
```

---

## List Doctors

```text
GET /api/doctors/
```

---

## Get Doctor

```text
GET /api/doctors/<id>/
```

Example:

```text
GET /api/doctors/1/
```

---

## Update Doctor

```text
PUT /api/doctors/<id>/
```

Example:

```text
PUT /api/doctors/1/
```

Request:

```json
{
    "name": "Dr. John Smith",
    "specialization": "Cardiology",
    "email": "johnsmith@example.com",
    "phone": "9876543210"
}
```

---

## Delete Doctor

```text
DELETE /api/doctors/<id>/
```

Example:

```text
DELETE /api/doctors/1/
```

---

# Patient-Doctor Mapping APIs

## Assign Doctor to Patient

```text
POST /api/mappings/
```

Request:

```json
{
    "patient": 1,
    "doctor": 1
}
```

This creates a relationship between the patient and doctor.

---

## List Mappings

```text
GET /api/mappings/
```

Returns patient-doctor mappings accessible to the authenticated user.

---

## Get Doctors Assigned to a Patient

```text
GET /api/mappings/<patient_id>/
```

Example:

```text
GET /api/mappings/1/
```

This returns all doctors assigned to patient `1`.

Example response:

```json
[
    {
        "id": 1,
        "patient": 1,
        "patient_name": "Alice Smith",
        "doctor": 1,
        "doctor_name": "Dr. Smith",
        "doctor_specialization": "Cardiology",
        "assigned_at": "2026-10-08T10:30:00Z"
    }
]
```

---

## Delete Mapping

```text
DELETE /api/mappings/<id>/
```

Example:

```text
DELETE /api/mappings/1/
```

This removes the specified patient-doctor relationship.

### Mapping URL Behavior

The assignment uses the same URL structure for the patient mapping lookup and mapping deletion:

```text
GET    /api/mappings/<patient_id>/
DELETE /api/mappings/<id>/
```

The HTTP method determines the operation.

For example:

```text
GET /api/mappings/1/
```

means:

> Get all doctors assigned to patient 1.

Whereas:

```text
DELETE /api/mappings/1/
```

means:

> Delete mapping with ID 1.

---

# API Authentication Example

For protected endpoints, include:

```text
Authorization: Bearer <ACCESS_TOKEN>
```

Example:

```text
GET /api/patients/
```

Headers:

```text
Authorization: Bearer eyJhbGciOiJIUzI1Ni...
Content-Type: application/json
```

---

# Testing with Postman

The APIs can be tested using Postman or any REST API client.

Recommended testing flow:

### 1. Register

```text
POST /api/auth/register/
```

### 2. Login

```text
POST /api/auth/login/
```

Copy the returned access token.

### 3. Add Authorization

For protected requests:

```text
Authorization: Bearer <access_token>
```

### 4. Create Patient

```text
POST /api/patients/
```

### 5. Create Doctor

```text
POST /api/doctors/
```

### 6. Assign Doctor to Patient

```text
POST /api/mappings/
```

### 7. Get Patient's Doctors

```text
GET /api/mappings/<patient_id>/
```

### 8. Delete Mapping

```text
DELETE /api/mappings/<mapping_id>/
```

---

# Automated Tests

The project includes automated tests using Django REST Framework's `APITestCase`.

Run the complete test suite:

```bash
python manage.py test
```

The test suite covers:

### Authentication

- User registration
- User login
- JWT token generation
- Duplicate email validation

### Patients

- Patient creation
- Patient listing
- Patient ownership
- Unauthenticated access protection
- Patient update
- Patient deletion

### Doctors

- Doctor creation
- Doctor listing
- Doctor update
- Doctor deletion

### Mappings

- Mapping creation
- Mapping listing
- Getting doctors assigned to a patient
- Duplicate mapping prevention
- Patient ownership validation
- Mapping deletion
- Mapping ownership/security

Expected result:

```text
Found 17 test(s).
.................
----------------------------------------------------------------------
Ran 17 tests in ...s

OK
```

The exact number of tests may increase if additional tests are added.

---

# Django System Check

Run:

```bash
python manage.py check
```

Expected result:

```text
System check identified no issues (0 silenced).
```

---

# Check for Missing Migrations

Run:

```bash
python manage.py makemigrations --check --dry-run
```

Expected result:

```text
No changes detected
```

---

# Django Admin

The Django Admin interface is available at:

```text
/admin/
```

For local development:

```text
http://127.0.0.1:8000/admin/
```

Create an administrator account using:

```bash
python manage.py createsuperuser
```

---

# Security

The project implements the following security measures:

- JWT authentication
- Password hashing through Django
- Protected API endpoints
- Custom user model
- Unique email addresses
- Patient ownership validation
- Mapping ownership validation
- Duplicate patient-doctor prevention
- Environment-based configuration
- `.env` excluded from Git
- Database-level unique constraint for mappings

---

# Authorization Rules

## Patients

A user can only:

- View their own patients
- Update their own patients
- Delete their own patients
- Assign doctors to their own patients

## Doctors

Authenticated users can:

- View doctors
- Create doctors
- Update doctors
- Delete doctors

## Mappings

A user can only:

- Create mappings for their own patients
- View mappings associated with their own patients
- Delete mappings associated with their own patients

This prevents users from accessing or modifying another user's patient relationships.

---

# Database Constraints

The patient-doctor mapping model uses a unique constraint:

```python
models.UniqueConstraint(
    fields=["patient", "doctor"],
    name="unique_patient_doctor"
)
```

This prevents duplicate assignments.

For example, this combination cannot be created twice:

```text
Patient 1 -> Doctor 1
Patient 1 -> Doctor 1
```

---

# Error Handling

The API uses Django REST Framework validation and standard HTTP status codes.

Examples include:

### Duplicate Email

```json
{
    "email": [
        "A user with this email already exists."
    ]
}
```

### Invalid Login

```json
{
    "non_field_errors": [
        "Invalid email or password."
    ]
}
```

### Unauthorized Patient Mapping

```json
{
    "patient": [
        "You can only assign doctors to your own patients."
    ]
}
```

### Duplicate Mapping

```json
{
    "non_field_errors": [
        "This doctor is already assigned to this patient."
    ]
}
```

---

# CORS

The project uses:

```text
django-cors-headers
```

for CORS support.

This allows the backend to be integrated with a frontend application in the future.

A frontend is **not required for this assignment**.

---

# Development Commands

## Start Server

```bash
python manage.py runserver
```

## Create Migrations

```bash
python manage.py makemigrations
```

## Apply Migrations

```bash
python manage.py migrate
```

## Run Tests

```bash
python manage.py test
```

## Run System Checks

```bash
python manage.py check
```

## Check Migrations

```bash
python manage.py makemigrations --check --dry-run
```

## Create Superuser

```bash
python manage.py createsuperuser
```

---

# Requirements

All Python dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# Environment File

A template environment file is provided as:

```text
.env.example
```

Copy it to:

```text
.env
```

and update the values according to your local PostgreSQL configuration.

Never commit sensitive information such as:

- Database passwords
- Django secret keys
- Production credentials
- API keys
- Authentication secrets

---

# Git and .gitignore

The following files and directories are excluded from Git:

```text
venv/
__pycache__/
*.py[cod]
*$py.class
.env
db.sqlite3
.idea/
.vscode/
*.log
staticfiles/
media/
.pytest_cache/
.coverage
htmlcov/
```

This prevents local environments, generated files, database files, and secrets from being committed.

---

# Frontend

This assignment focuses on the backend API.

Therefore, this repository does not contain a frontend application.

The API can be consumed using:

- Postman
- Insomnia
- curl
- Django REST Framework Browsable API
- Any frontend application in the future

---

# Assignment Requirements Coverage

| Requirement | Status |
|---|---|
| Django | Completed |
| Django REST Framework | Completed |
| PostgreSQL | Completed |
| Django ORM | Completed |
| Environment variables | Completed |
| JWT Authentication | Completed |
| User Registration | Completed |
| User Login | Completed |
| Patient CRUD | Completed |
| Doctor CRUD | Completed |
| Patient-Doctor Mapping | Completed |
| Mapping Deletion | Completed |
| Patient Mapping Lookup | Completed |
| Input Validation | Completed |
| Authorization | Completed |
| Ownership Controls | Completed |
| Automated Tests | Completed |
| Error Handling | Completed |
| README Documentation | Completed |
| Frontend | Not required |

---

# Future Improvements

Possible future improvements include:

- Swagger/OpenAPI documentation
- API pagination
- Advanced filtering and searching
- Rate limiting
- Production-specific CORS configuration
- Refresh token rotation
- Docker support
- CI/CD using GitHub Actions
- Cloud deployment
- Role-based permissions
- More comprehensive API integration tests

These improvements are not required for the current assignment.

---

# Author

**Antony Johny**

GitHub Repository:

https://github.com/AntonyJohny/whatbytes-healthcare-backend

---

# License

This project was created for educational and assignment purposes.
