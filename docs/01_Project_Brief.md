Project Brief: Job & Employability Progression Management System (JEPMS)
1. Project Overview
The Job & Employability Progression Management System (JEPMS) is a web-based application developed using Python and Django. It is designed to help manage employer information, job vacancies and job applications through a centralised system.

The application provides a structured way to store, view, add, update and delete records. It also includes user authentication to restrict access to authorised users.

The project demonstrates the application of software development principles, including requirements analysis, database design, implementation, testing, security, deployment and documentation.

2. Business Problem
Managing employer details, job vacancies and job applications manually can lead to several problems:

Information may be stored across multiple spreadsheets or documents.
Updating employer and vacancy details can become time-consuming.
Job application records may be difficult to track and maintain.
Duplicate or inconsistent information may occur.
Unauthorised users may access or modify sensitive records.
Reporting and reviewing employment opportunities may require additional manual effort.
A centralised web application can reduce these problems by providing a consistent way to manage employment-related information.

3. Project Objectives
The main objectives of JEPMS are to:

Develop a functional web application using Python and Django.
Create a database to store employer, vacancy and job application information.
Implement CRUD operations (Create, Read, Update and Delete) for the main records.
Establish relationships between employers, vacancies and job applications.
Provide user authentication to protect application access.
Validate user input and handle common errors appropriately.
Test the application's main functionality and document the results.
Deploy the application to a suitable hosting platform, such as PythonAnywhere.
Provide clear technical documentation and a user guide.
4. Project Scope
4.1 In Scope
The project will include:

Employer management, including adding, viewing, updating and deleting employer records.
Vacancy management, including recording job titles, descriptions and related details.
Job application management, including linking applications to relevant vacancies.
Database storage using SQLite during development.
Django models, views, templates and URL routing.
User login and access control.
Basic form validation and error handling.
Functional testing of important application features.
Deployment preparation and deployment documentation.
A README file and user guide.
4.2 Out of Scope
The following features are not required for the initial version:

Integration with external job portals.
Online payment processing.
Automated CV screening or candidate ranking using AI.
Email and SMS notifications.
Advanced analytics and reporting dashboards.
A dedicated mobile application.
Complex multi-organisation permissions.
These features may be considered for future development.

5. Stakeholders
Stakeholder	Role and Interest
System administrator	Manages access and maintains application records.
Recruitment staff	Maintain employer details, vacancies and application information.
Employers	Represent organisations offering job vacancies.
Job applicants	Are represented through application records maintained in the system.
Developer	Designs, implements, tests, documents and deploys the application.
Assessor or tutor	Reviews the project, development evidence and achievement of requirements.
6. Assumptions and Constraints
Assumptions
Users have access to a computer and a modern web browser.
Authorised users will enter accurate and relevant information.
Employer, vacancy and application records will be maintained by permitted users.
Each vacancy will be associated with an employer.
Each job application will be associated with an appropriate vacancy.
The initial application will use SQLite for straightforward development and demonstration.
The deployment environment will support the selected Python and Django versions.
Constraints
The project must be completed within the available development time.
The initial version will use a relatively simple database and application structure.
The system will be developed using Python and Django.
Testing and deployment evidence must be documented.
The deployed application will depend on the configuration and limitations of the selected hosting service.
7. Success Criteria
The project will be considered successful when the following criteria are met:

The application starts successfully in the development environment.
Users can authenticate before accessing protected functionality.
Employer records can be created, viewed, updated and deleted.
Vacancy records can be managed and linked to employers.
Job application records can be managed and linked to vacancies.
Required fields and invalid input are handled appropriately.
Database relationships operate correctly and prevent invalid references where applicable.
Automated tests cover the main models, views and application workflows.
The application is deployed successfully, or deployment steps and any unresolved issues are documented.
The README, user guide, test evidence and project documentation are complete.
The final application demonstrates the intended business purpose and meets the agreed scope.
8. Deliverables
The expected project deliverables are:

A working Django web application.
Django models and database configuration.
Templates, views, URL routes and forms.
User authentication and access control.
Automated tests and test results.
A configured database for development.
Deployment instructions and deployment evidence.
README.md containing project setup and usage information.
A user guide explaining how to use the application.
Supporting capstone evidence and a final reflection.
9. Project Summary
JEPMS aims to provide a simple, centralised solution for managing employer details, job vacancies and job applications. The project will demonstrate the full software development process, from identifying a business problem and defining requirements to building, testing, documenting and deploying a web application.

The initial release will focus on reliable core functionality, maintainable code, appropriate data relationships and secure access. Additional features can be introduced after the core requirements have been completed and tested.