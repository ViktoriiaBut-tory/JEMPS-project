# Job & Employability Progression Management System (JEPMS)

## Project Overview

JEPMS is a web application developed using Python and Django.

The main purpose of this project is to help users manage their job search, track job applications, and monitor their employability progress.

This project is being developed as part of the Level 3 Software Development course.

## Business Problem

Job seekers often use different websites, emails, and documents to manage their job applications.

This can make it difficult to track applications, interviews, and progress.

JEPMS aims to provide one place where users can organise their job search information.

## Target Users

The application is designed for:

- Job seekers
- Students and trainees
- Career advisers
- Administrators

## Planned Features

### Must Have
- User registration and login
- User authentication
- Add and manage job applications
- View application details
- Update application status
- Delete job applications

### Should Have
- Track employability skills
- Record training activities
- Search and filter job applications
- View personal progress

### Could Have
- Progress dashboard
- Interview reminders
- Reports and statistics

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap
- Git and GitHub

## Project Structure

```text
JEMPSproject/
├── JEPMSproject/
├── applications/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ViktoriiaBut-tory/JEMPSproject.git
```

### 2. Open the project folder

```bash
cd JEMPSproject
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

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open the application at:

`http://127.0.0.1:8000/`

## Project Status

**In Development**

The project is currently being developed and tested.

## Future Improvements

- Improve the user interface
- Add more employability tracking features
- Implement automated testing
- Prepare the application for deployment

## Author

Developed as part of the Level 3 Software Development course.