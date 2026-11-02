# 07 – Deployment

## 1. Introduction

I deployed my Job & Employability Progression Management System (JEPMS) to PythonAnywhere.

The purpose of deployment was to make the Django application available online and test it outside my local development environment.

**Live website:** https://viktoriiabut.pythonanywhere.com

**GitHub repository:** https://github.com/ViktoriiaBut-tory/JEMPS-project

## 2. Deployment Environment

I used the following tools and technologies:

- PythonAnywhere – web hosting platform.
- Python 3.13.1 – Python version on the server.
- Django 6.1.2 – web framework.
- Git and GitHub – source code management.
- SQLite – database.
- Python virtual environment – project dependencies.
- WSGI – connection between Django and the web server.

## 3. Preparing the Project

Before deployment, I checked the project locally.

I ran:

`python manage.py check`

The result was:

`System check identified no issues (0 silenced).`

I also ran 18 automated tests, and all tests passed.

I updated the Django settings to use environment variables for `DEBUG` and `ALLOWED_HOSTS`.

I checked that `.env` was excluded from GitHub.

## 4. Uploading the Project to GitHub

I committed the latest changes and pushed them to the main branch.

Commands used:

```bash
git add JEPMSproject/settings.py
git commit -m "Prepare Django settings for PythonAnywhere deployment"
git push origin main
```

The deployment preparation commit was:

`de0afda`

I checked that the working tree was clean before deployment.

## 5. Cloning the Project to PythonAnywhere

I opened a Bash Console on PythonAnywhere and cloned the GitHub repository.

```bash
git clone https://github.com/ViktoriiaBut-tory/JEMPS-project.git
cd JEMPS-project
```

I checked that the project files were present, including `manage.py`, `applications`, `templates` and `requirements.txt`.

## 6. Creating the Virtual Environment

I created a virtual environment using Python 3.13.

```bash
python3.13 -m venv venv
source venv/bin/activate
```

I installed the project dependencies:

```bash
python -m pip install -r requirements.txt
```

I confirmed the Django version:

```bash
python -m django --version
```

Result: `6.1.2`

## 7. Environment Variables

I created a separate `.env` file on PythonAnywhere.

It contains configuration values for:

- `SECRET_KEY`
- `DEBUG`
- `DJANGO_ALLOWED_HOSTS`

I set `DEBUG=False` for the deployed application and configured the PythonAnywhere domain in `ALLOWED_HOSTS`.

I did not upload the `.env` file to GitHub.

## 8. Database Setup

I used Django migrations to create the database tables.

```bash
python manage.py migrate
python manage.py showmigrations applications
```

The application migrations were successfully applied:

```text
[X] 0001_initial
[X] 0002_alter_jobapplication_learner_email
```

I also created a new Django superuser on PythonAnywhere because the server uses a separate database from my local computer.

## 9. Web Application Configuration

My PythonAnywhere Beginner plan allows one web application.

I reused the existing web application previously configured for a Django To-Do project.

Before changing the configuration, I created a backup of the old WSGI file.

I updated the following paths:

**Source code and working directory:**

`/home/viktoriiabut/JEMPS-project`

**Virtual environment:**

`/home/viktoriiabut/JEMPS-project/venv`

**WSGI configuration file:**

`/var/www/viktoriiabut_pythonanywhere_com_wsgi.py`

I updated the WSGI configuration to load:

`JEPMSproject.settings`

After saving the changes, I reloaded the website.

## 10. Deployment Problem and Solution

**Problem: Bad Request (400)**

When I first opened the deployed website, Django displayed a Bad Request (400) error.

**Investigation:**

I checked the allowed hosts configuration using:

```bash
python manage.py shell -c "from django.conf import settings; print(settings.ALLOWED_HOSTS)"
```

I found that the domain name in the environment variable was incomplete.

**Solution:**

I corrected `DJANGO_ALLOWED_HOSTS` in the server's `.env` file and reloaded the web application.

**Result:**

The website opened successfully.

## 11. Deployment Verification

I tested the live application using a web browser.

The following functions worked successfully:

- Login and logout.
- Dashboard and navigation.
- Creating employers.
- Creating vacancies.
- Creating job applications.
- Editing and deleting records.
- Saving data to the SQLite database.
- Updating dashboard totals.

The Bootstrap styling also displayed correctly.

## 12. Known Limitations

The deployed application is an educational demonstration project.

Some production security recommendations still need further review, including HTTPS-related settings and the email backend.

The SQLite database is suitable for this small demonstration, but a larger application may require a different database system.

The application should use fictional test data until the remaining production security checks are completed.

## 13. Deployment Result

I successfully deployed JEPMS to PythonAnywhere.

The application is accessible online, and its main features work correctly.

This task helped me understand the differences between local development and deployment, how to configure a Django application on a server, and how to investigate deployment errors.