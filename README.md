# WhatBytes Healthcare Backend

A secure and scalable healthcare backend API built using **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT authentication**.

This project was developed as part of the **WhatBytes Full Stack Intern Assignment – Django Healthcare Backend**.

The application provides APIs for:

- User registration and authentication
- JWT-based authentication
- Patient management
- Doctor management
- Patient-doctor mappings
- Input validation
- Ownership and authorization
- PostgreSQL database integration
- Automated API tests

---

## Tech Stack

- **Python 3**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Django ORM**
- **Simple JWT**
- **python-dotenv**
- **django-cors-headers**
- **psycopg2-binary**

---

## Features

### Authentication

- User registration
- User login
- JWT access and refresh tokens
- Password hashing using Django's authentication system
- Custom user model using email as the username
- Protected API endpoints
- Session authentication for Django REST Framework's browser interface

### Patients

Authenticated users can:

- Create patients
- View their patients
- View individual patients
- Update patients
- Delete patients

Patient records are associated with the user who created them.

Users cannot access or modify patients belonging to another user.

### Doctors

Authenticated users can:

- Create doctors
- View doctors
- View individual doctors
- Update doctors
- Delete doctors

### Patient-Doctor Mappings

Authenticated users can:

- Assign doctors to patients
- View all mappings available to them
- View doctors assigned to a specific patient
- Remove doctor assignments
- Prevent duplicate patient-doctor assignments

Users can only create or delete mappings involving their own patients.

### Validation

The API includes validation for:

- Required fields
- Email format
- Duplicate email addresses
- Password length
- Patient ownership
- Duplicate patient-doctor mappings
- Doctor/patient relationships
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
