# 05 – Testing

## 1. Introduction

Testing was an important part of my JEPMS project. I used Django's built-in testing framework to check that the application works correctly.

The main purpose of testing was to find errors, check data validation and make sure that users can access the correct pages.

## 2. Testing Tools

I used the following tools:

- **Django TestCase** – to create automated tests.
- **Django Test Client** – to test web pages and HTTP responses.
- **VS Code Terminal** – to run tests and check results.
- **Web Browser** – to test the application manually.

All automated tests were written in the `applications/tests.py` file.

## 3. Model Testing

I tested the three main database models:

- Employer
- Vacancy
- JobApplication

The tests checked that objects could be created and that their information was saved correctly.

## 4. Form Testing

I tested Django ModelForms to check data validation.

The tests included:

- Checking valid employer information.
- Checking invalid email addresses.
- Checking vacancy form data.
- Checking job application form validation.

These tests helped confirm that the application accepts correct information and rejects invalid data.

## 5. View Testing

I tested the main application views.

The tests checked:

- Whether list pages return HTTP status code 200 for authenticated users.
- Whether unauthenticated users are redirected to the login page.
- Whether the correct HTML templates are used.
- Whether records can be created and updated.

I used `force_login()` in tests to simulate an authenticated user.

## 6. CRUD Testing

I tested the Create, Read, Update and Delete functionality through the web interface.

I checked that users could:

- Add new employers, vacancies and job applications.
- View saved information.
- Edit existing records.
- Delete records using confirmation pages.

## 7. Test Execution

I ran the automated tests using the following command:

`python manage.py test applications`

The final test result was:

```text
Found 18 test(s).

Ran 18 tests in 2.942s

OK
```

All 18 automated tests passed successfully.

## 8. Problems and Solutions

During development, I found several problems.

**Problem 1: Indentation errors**

Some tests failed because Python indentation was incorrect.

**Solution:** I corrected the indentation and ran the tests again.

**Problem 2: Authentication redirects**

Some view tests returned HTTP status code 302 instead of 200.

**Solution:** I checked the login requirements and used `force_login()` for authenticated view tests.

**Problem 3: Form validation**

Some invalid form data was not handled as expected.

**Solution:** I reviewed the form fields, validation rules and error messages.

## 9. Manual Testing After Deployment

After deploying JEPMS to PythonAnywhere, I tested the live application.

I successfully checked:

- User login and logout.
- Dashboard and navigation.
- Creating employers.
- Creating vacancies.
- Creating job applications.
- Saving and displaying records.
- Editing and deleting records.

The application worked correctly during these checks.

## 10. Testing Result

The automated tests passed, and the main application functions worked during manual testing.

Testing helped me identify problems, improve the application and confirm that the main requirements were met.