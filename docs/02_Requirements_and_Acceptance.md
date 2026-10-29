02 — Requirements and Acceptance Criteria
1. Project Overview
Project Name: Job & Employability Progression Management System (JEPMS)

Purpose: The system will help authorised users manage employer details, job vacancies, and learner job applications through a simple web-based application developed using Django.

Target Users: Tutors, employability staff, and other authorised users responsible for maintaining employer and job application records.

2. Functional Requirements
Functional requirements describe what the system must do.

ID	Requirement	Priority
FR01	The system shall allow an authorised user to log in and log out securely.	Must
FR02	The system shall redirect unauthenticated users away from protected pages to the login page.	Must
FR03	The system shall list employers and allow a user to view an employer's details.	Must
FR04	The system shall allow authorised users to create, view, update, and delete employer records.	Must
FR05	The system shall allow authorised users to create, view, update, and manage vacancies linked to an employer.	Must
FR06	The system shall allow authorised users to create, view, update, and manage job applications linked to a vacancy.	Must
FR07	The system shall validate required fields, email formats where relevant, dates, and permitted status values.	Must
FR08	The system shall provide search and filtering for job applications by learner name, employer or vacancy, and application status where practical.	Must
FR09	The system shall display clear success and validation messages after user actions.	Must
3. Non-Functional Requirements
Non-functional requirements describe how the system should perform and the standards it should meet.

ID	Requirement	Priority
NFR01	The application shall provide a simple, consistent interface that is easy for a beginner or first-time user to navigate.	Must
NFR02	Protected pages and record-management actions shall require authentication.	Must
NFR03	The application shall use Django forms and server-side validation to validate submitted data.	Must
NFR04	The application shall store records in a relational database using Django models and appropriate relationships.	Must
NFR05	The application shall use Django's built-in protection against common web vulnerabilities, including CSRF, when forms change data.	Must
NFR06	The application shall use reusable templates and static CSS to maintain a consistent appearance.	Should
NFR07	The application shall display useful error messages without exposing passwords, secret keys, or technical debugging details to users.	Must
NFR08	The application shall be tested using Django tests or an equivalent documented test process.	Must
NFR09	The application shall include setup instructions, dependencies, and instructions for running the project locally.	Must
NFR10	The application shall be suitable for deployment to a compatible hosting environment.	Should
4. User Stories
US01 — User Authentication
As an authorised user,
I want to log in and log out,
So that I can access the system securely.

Acceptance Criteria

Given a registered user with valid credentials, when they submit the login form, then they are logged in successfully.
Given a user enters invalid credentials, when they submit the form, then an appropriate error message is displayed.
Given a logged-in user, when they select Logout, then their session ends and they are returned to the login page.
Given an unauthenticated visitor, when they try to access a protected page, then they are redirected to login.
US02 — View Employers
As an authorised user,
I want to view a list of employers and their details,
So that I can find relevant employer information.

Acceptance Criteria

Given employer records exist, when the user opens the employer list, then the records are displayed.
Given the user selects an employer, then the employer's stored details are displayed.
Given no employers exist, then the system displays a helpful empty-state message.
US03 — Manage Employers
As an authorised user,
I want to add, edit, and delete employer records,
So that employer information remains accurate and up to date.

Acceptance Criteria

Given valid employer details, when the user submits the form, then the employer record is saved.
Given an existing employer, when the user edits and saves valid details, then the updated details are displayed.
Given an employer record, when the user requests deletion and confirms the action, then the record is deleted if permitted by the system's relationship rules.
Given invalid or missing required data, then the record is not saved and validation errors are displayed.
US04 — Manage Vacancies
As an authorised user,
I want to create and maintain vacancies linked to employers,
So that available job opportunities can be tracked.

Acceptance Criteria

Given an existing employer, when the user creates a vacancy and selects that employer, then the vacancy is saved with the correct employer relationship.
Given a vacancy exists, when the user opens its details, then its title, description, location, closing date, status, and employer are displayed where applicable.
Given a vacancy is edited, when valid changes are submitted, then the updated information is saved.
Given invalid data, then the system displays validation errors and does not save the invalid changes.
Given a vacancy has related applications, then the system prevents accidental deletion where required by the configured relationship rules.
US05 — Manage Job Applications
As an authorised user,
I want to create and maintain job applications linked to vacancies,
So that learner application progress can be monitored.

Acceptance Criteria

Given an existing vacancy, when the user creates an application and selects that vacancy, then the application is saved with the correct relationship.
Given an application exists, when the user views it, then the learner details, vacancy, application date, status, and notes are displayed where applicable.
Given an application exists, when the user updates its status, then the new status is saved and displayed.
Given required fields are missing or invalid, then the system displays validation errors.
Given an application is deleted, then the system removes it only after the required confirmation.
US06 — Validate Data
As an authorised user,
I want to receive validation when I enter incorrect data,
So that the system maintains reliable records.

Acceptance Criteria

Required fields cannot be submitted empty.
Email fields reject incorrectly formatted email addresses.
Dates are validated according to the agreed business rules.
Vacancy and application status fields accept only the defined status choices.
Invalid submissions show useful error messages and do not save invalid data.
US07 — Search and Filter Applications
As an authorised user,
I want to search and filter job applications,
So that I can quickly find a learner's application or review applications by status.

Acceptance Criteria

The user can search applications using a learner's name.
The user can filter applications by vacancy or employer where implemented.
The user can filter applications by status.
When matching records exist, the results show only the records matching the selected search or filter criteria.
When no records match, the system displays a message explaining that no results were found.
The user can clear the search or filters to return to the full application list.
US08 — Display Feedback Messages
As an authorised user,
I want to receive feedback after completing an action,
So that I know whether the action succeeded or needs correction.

Acceptance Criteria

A successful create or update action displays a success message.
A successful deletion displays a confirmation message.
Invalid form submissions display relevant field-level or form-level errors.
Messages are clear and do not expose sensitive technical information.
5. Data Requirements
The system shall maintain the following main data entities.

Employer
Employer name
Contact name
Email address
Phone number
Website
Notes
Vacancy
Employer relationship
Job title
Description
Location
Closing date, where applicable
Vacancy status: Open, Closed, or On Hold
Job Application
Learner name
Learner email
Vacancy relationship
Application date
Application status: Draft, Applied, Interview, Offer, Rejected, or Withdrawn
Notes
Created and updated timestamps
Relationships
One employer can have multiple vacancies.
One vacancy belongs to one employer.
One vacancy can have multiple job applications.
One job application belongs to one vacancy.
The system shall use Django models and foreign keys to maintain these relationships.

6. Business Rules
ID	Business Rule
BR01	Each vacancy must be linked to an existing employer.
BR02	Each job application must be linked to an existing vacancy.
BR03	Vacancy and application statuses must use the defined status choices.
BR04	Required fields must contain valid values before records are saved.
BR05	An application date must not be in the future unless the project requirements are deliberately changed.
BR06	A vacancy closing date must follow the agreed date-validation rules.
BR07	Related records must not be deleted in a way that unintentionally removes dependent data.
BR08	Only authorised users may access protected management pages and perform protected actions.
7. Scope and Limitations
Included in the Project
Login and logout.
Employer management.
Vacancy management.
Job application management.
Form validation and feedback messages.
Basic search and filtering.
Database relationships.
Testing and project documentation.
Outside the Initial Scope
Automatic job-board integration.
Email notifications to learners or employers.
CV parsing or AI-based job matching.
Online applications submitted directly by learners.
Advanced analytics and reporting dashboards.
Multiple organisational roles with complex permissions.
These features may be considered as future improvements if time allows.

8. Requirements Traceability
The following table links the requirements to planned implementation and testing.

Requirement	Planned Implementation	Evidence of Completion
FR01	Django authentication views and logout	Login and logout tests
FR02	Login protection for views	Unauthenticated access test
FR03	Employer list and detail views	Employer list and detail tests
FR04	Employer forms and CRUD views	Create, view, update, and delete tests
FR05	Vacancy forms, views, and employer foreign key	Vacancy CRUD and relationship tests
FR06	Application forms, views, and vacancy foreign key	Application CRUD and relationship tests
FR07	Django form and model validation	Valid and invalid form tests
FR08	Search and filter logic in the application list	Search and filter tests
FR09	Django messages framework and form errors	Success and validation message tests
NFR01, NFR06	Shared templates and CSS	Interface review
NFR02, NFR05	Authentication and Django security features	Access-control and form-security checks
NFR04	Django ORM and relational database	Database and relationship tests
NFR07	Safe error handling and production settings	Error-handling review
NFR08	Automated tests and documented manual checks	Test results
NFR09, NFR10	README, dependency file, and deployment instructions	Setup and deployment evidence
9. Definition of Done
The project will be considered complete when:

All Must-have functional requirements have been implemented.
Users can authenticate and access protected pages appropriately.
Employer, vacancy, and job application records can be managed.
The required relationships between records work correctly.
Forms validate input and display useful feedback.
Search and filtering work for the implemented criteria.
The main functional requirements have been tested.
The README explains installation, database setup, and how to run the application.
No known critical errors remain in the tested core workflows.