# 04 – Implementation

## 1. Introduction

The JEPMS project was developed using Python and Django. The purpose of the application is to help users manage employers, job vacancies and job applications in one system.

I used Visual Studio Code to write the code and GitHub to manage the project versions.

## 2. Project Structure

The project contains a Django application called `applications`.

The main files are:

- `models.py` – defines the database models.
- `forms.py` – contains forms for entering and editing data.
- `views.py` – handles requests and application logic.
- `urls.py` – connects URLs to views.
- `admin.py` – registers models in Django Admin.
- `tests.py` – contains automated tests.
- `templates/` – contains HTML pages.
- `docs/` – contains project documentation.

## 3. Database Models

I created three main models:

**Employer:** Stores company details, including name, contact information and notes.

**Vacancy:** Stores job information, including title, employer, location, closing date and status.

**JobApplication:** Stores learner details, the selected vacancy, application date, status and notes.

I used ForeignKey relationships to connect vacancies to employers and job applications to vacancies.

## 4. Forms and Validation

I created ModelForms to allow users to add and update information.

Django forms help validate user input. For example, email fields check that an email address has a valid format.

If the information is invalid, the form displays an error message.

## 5. Views and CRUD Operations

The application supports four main operations:

- **Create** – add new records.
- **Read** – display records.
- **Update** – edit existing records.
- **Delete** – remove records.

I used function-based views for lists and the dashboard. I also used Django class-based views for creating, updating and deleting records.

## 6. User Authentication

The application uses Django authentication.

Users must log in before accessing the main application pages.

I used `login_required` and `LoginRequiredMixin` to protect the views.

## 7. Dashboard

I created a dashboard that displays the total number of employers, vacancies and job applications.

The dashboard also provides navigation buttons to the main sections.

## 8. User Interface

I used HTML templates and Bootstrap to create a simple and responsive interface.

The navigation bar allows users to move between Dashboard, Employers, Vacancies and Applications.

## 9. Version Control

I used Git and GitHub to save the project and track changes.

I also used GitHub Projects Kanban to organise tasks into To Do, In Progress and Done.

The `.gitignore` file excludes local files such as the virtual environment, database and `.env` file.

## 10. Implementation Result

The main application features were completed successfully.

Users can log in, manage employers, vacancies and job applications, and view information on the dashboard.

The application was also deployed to PythonAnywhere for online access.