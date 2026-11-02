# 06 – Security

## 1. Introduction

Security is an important part of the JEPMS project because the application stores employer information, job vacancies and learner details.

I used Django's built-in security features to protect the application and control user access.

## 2. User Authentication

JEPMS uses Django's authentication system.

Users must log in before accessing the main application pages.

I used:

- `login_required` for function-based views.
- `LoginRequiredMixin` for class-based views.
- Django's built-in Login and Logout views.

This helps prevent unauthorised users from accessing the main application.

## 3. CSRF Protection

CSRF means Cross-Site Request Forgery.

It is an attack where another website tries to make a user perform an action without their permission.

Django provides built-in CSRF protection.

I used `{% csrf_token %}` in HTML forms that submit data using POST requests.

This helps protect actions such as creating, editing and deleting records.

## 4. XSS Protection

XSS means Cross-Site Scripting.

It happens when malicious scripts are added to a website through user input.

Django templates automatically escape HTML characters by default.

I used Django templates to display data safely and did not intentionally disable automatic escaping.

## 5. Environment Variables

I used a `.env` file to store configuration values.

The file contains settings such as:

- `SECRET_KEY`
- `DEBUG`
- `DJANGO_ALLOWED_HOSTS`

I used `python-dotenv` to load these values into Django.

The `.env` file is included in `.gitignore`, so it is not uploaded to GitHub through normal Git operations.

## 6. SECRET_KEY Protection

Django uses `SECRET_KEY` for important security functions.

I stored the key outside the source code and loaded it from an environment variable.

I did not include the secret value in the project documentation.

## 7. DEBUG Setting

During local development, I used:

`DEBUG=True`

For deployment on PythonAnywhere, I changed this to:

`DEBUG=False`

This prevents Django from showing detailed debugging information to website visitors.

## 8. ALLOWED_HOSTS

I configured `ALLOWED_HOSTS` to specify which domain names can access the application.

On PythonAnywhere, I used:

`viktoriiabut.pythonanywhere.com`

During deployment, I received a Bad Request (400) error because the domain name was incomplete.

I corrected the environment variable and reloaded the web application.

The website then worked correctly.

## 9. Database Security

The project uses SQLite.

The database file is excluded from GitHub using `.gitignore`.

The application uses Django's ORM to work with database records instead of building SQL queries from untrusted user input.

## 10. Production Security Review

I used Django's deployment check to review security settings:

`python manage.py check --deploy`

The check identified settings that required attention before production deployment.

For this educational project, the following areas still need a final production review:

- HTTPS redirects.
- Secure session and CSRF cookies.
- HSTS configuration.
- Production email backend.

The application is deployed for learning and demonstration purposes. Passing functional tests does not mean that every production security recommendation has been completed.

## 11. Security Result

JEPMS includes authentication, CSRF protection, Django template escaping and environment-based configuration.

I also learned how to identify deployment security warnings and how to protect sensitive configuration values.

Further security checks would be required before using the application with real personal information.