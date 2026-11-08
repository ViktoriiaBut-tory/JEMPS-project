# Job & Employability Progression Management System (JEPMS)

## Project Overview

JEPMS is a web application developed using Python, Django and FastAPI as part of the Level 3 Software Development course.

The main purpose of the project is to help users organise job search information, manage employers and vacancies, track job applications and monitor their progress.

The project includes a Django web interface and a FastAPI REST API. Both use the same SQLite database.

## Business Problem

Job seekers often use different websites, emails and documents to manage their job applications.

This can make it difficult to track vacancies, application statuses and interview opportunities.

JEPMS provides one central place where users can organise and update their job search information.

## Target Users

The application is designed for:

- Job seekers
- Students and trainees
- Career advisers
- Administrators

## Implemented Features

### Django Web Application

- User login and logout
- User authentication
- Add, view, edit and delete employers
- Add, view, edit and delete vacancies
- Add, view, edit and delete job applications
- Update application statuses
- Dashboard with an overview of records
- Forms with data validation
- Django administration interface

### FastAPI REST API

FastAPI was integrated into the existing Django project to provide API access to the same database.

The API supports CRUD operations for three models:

| Model | GET | POST | PUT | DELETE |
|---|---|---|---|---|
| Employers | Yes | Yes | Yes | Yes |
| Vacancies | Yes | Yes | Yes | Yes |
| JobApplications | Yes | Yes | Yes | Yes |

The API uses Pydantic schemas to validate input data and return structured JSON responses.

API endpoints can be explored and tested using Swagger UI.

**Note:** FastAPI is intended for local demonstration only. Authentication has not been implemented for the API, so it should not be publicly deployed in its current form.

## Technologies

- Python
- Django
- FastAPI
- Pydantic
- SQLite
- Django ORM
- HTML, CSS and Bootstrap
- pytest
- pytest-django
- FastAPI TestClient
- Git and GitHub
- VS Code

## Project Structure

```text
JEMPSproject/
├── JEPMSproject/
├── applications/
├── api/
│   ├── models/
│   │   ├── employer_schema.py
│   │   ├── vacancy_schema.py
│   │   └── job_application_schema.py
│   ├── routers/
│   │   ├── employers_router.py
│   │   ├── vacancies_router.py
│   │   └── job_applications_router.py
│   ├── tests/
│   │   ├── test_main.py
│   │   ├── test_employers.py
│   │   ├── test_vacancies.py
│   │   └── test_job_applications.py
│   └── main.py
├── docs/
├── manage.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ViktoriiaBut-tory/JEMPS-project.git
```

### 2. Open the project folder

```bash
cd JEMPS-project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows Git Bash:

```bash
source venv/Scripts/activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure environment variables

Create a local `.env` file with the Django configuration required by the project, including the secret key.

Do not upload `.env` to GitHub.

### 7. Apply database migrations

```bash
python manage.py migrate
```

### 8. Create an administrator account

```bash
python manage.py createsuperuser
```

## Running the Django Application

Start the Django development server:

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

Log in to manage employers, vacancies and job applications.

## Running FastAPI

Stop the Django development server before starting FastAPI on the same port.

Run:

```bash
fastapi dev api/main.py
```

Open Swagger UI:

http://127.0.0.1:8000/docs

Swagger UI allows users to test API endpoints and view JSON responses.

FastAPI and Django use the same database models through Django ORM.

## Automated Testing

The project includes automated tests for both Django and FastAPI.

### Django Tests

18 tests cover the main Django application functionality.

### FastAPI Tests

12 tests cover:

- Main API endpoint
- Employer retrieval and creation
- Vacancy retrieval and creation
- Job application retrieval and creation
- Updating job applications
- Deleting job applications
- Error handling for missing records

FastAPI tests use pytest, TestClient and a separate Django test database.

### Run All Tests

```bash
python -m pytest -v
```

**Latest verified result: 30 tests passed.**

This includes 18 Django tests and 12 FastAPI tests.

## Challenges and Solutions

During development, I experienced several technical challenges.

**Django and FastAPI integration:** I needed to initialise Django before importing API routers that use Django models.

**Database locking during tests:** SQLite reported a database locking error. I resolved this by using `@pytest.mark.django_db(transaction=True)` in FastAPI database tests.

**Test discovery:** I updated `pytest.ini` so pytest could discover both Django and FastAPI tests.

These challenges helped me improve my debugging, problem-solving and testing skills.

## Project Status

The main Django application and local FastAPI integration are implemented.

All 30 automated tests passed in the latest combined test run.

The Django application has also been deployed to PythonAnywhere. FastAPI remains a local demonstration component.

## Future Improvements

- Improve the user interface
- Add search and filtering options
- Introduce more employability tracking features
- Add reports and statistics
- Add authentication before any public FastAPI deployment
- Expand automated test coverage

## Reflection

This project helped me develop practical skills in Python, Django, FastAPI, database management and automated testing.

I learned how to build a web application, create REST API endpoints, connect different frameworks to the same database and test application functionality.

I also gained experience using GitHub, solving technical problems and organising a software development project.

## Author

Developed as part of the Level 3 Software Development course.