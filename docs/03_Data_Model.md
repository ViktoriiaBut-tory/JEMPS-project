03 — Data Model
1. Introduction
The Job & Employability Progression Management System (JEPMS) uses a relational database to store employer details, job vacancies, and learner job applications.

The application uses three Django models:

Employer
Vacancy
JobApplication
Each model represents a database table. Django automatically creates a primary key named id unless a different primary key is specified.

2. Entity and Field Definitions
2.1 Employer
The Employer model stores information about organisations that advertise job vacancies.

Field	Data Type	Description
id	AutoField / BigAutoField	Primary key generated automatically by Django
name	CharField	Employer or organisation name
contact_name	CharField	Name of the employer's contact person
email	EmailField	Employer contact email address
phone	CharField	Employer contact telephone number
website	URLField	Employer website address
notes	TextField	Additional information about the employer
Primary key: id

Relationship: One employer can have multiple vacancies.

2.2 Vacancy
The Vacancy model stores job opportunities advertised by employers.

Field	Data Type	Description
id	AutoField / BigAutoField	Primary key generated automatically by Django
employer	ForeignKey	Links the vacancy to an existing employer
title	CharField	Job title
description	TextField	Details about the job
location	CharField	Job location
closing_date	DateField	Application closing date; optional
status	CharField with choices	Open, Closed, or On Hold
Primary key: id

Foreign key: employer_id references Employer.id.

Relationship: Each vacancy belongs to one employer, while an employer can have multiple vacancies.

The foreign key uses on_delete=PROTECT to prevent deletion of an employer while dependent vacancies exist.

2.3 JobApplication
The JobApplication model stores learner applications linked to job vacancies.

Field	Data Type	Description
id	AutoField / BigAutoField	Primary key generated automatically by Django
learner_name	CharField	Name of the learner
learner_email	EmailField	Learner's email address
vacancy	ForeignKey	Links the application to a vacancy
application_date	DateField	Date of application
status	CharField with choices	Draft, Applied, Interview, Offer, Rejected, or Withdrawn
notes	TextField	Additional application notes
created_at	DateTimeField	Date and time the record was created
updated_at	DateTimeField	Date and time the record was last updated
Primary key: id

Foreign key: vacancy_id references Vacancy.id.

Relationship: Each application belongs to one vacancy, while a vacancy can have multiple applications.

The foreign key uses on_delete=PROTECT to prevent deletion of a vacancy while dependent applications exist.

3. Relationship Summary
Entity	Relationship	Related Entity
Employer	One-to-many (1:N)	Vacancy
Vacancy	Many-to-one (N:1)	Employer
Vacancy	One-to-many (1:N)	JobApplication
JobApplication	Many-to-one (N:1)	Vacancy
Explanation
One employer can advertise several vacancies.
Each vacancy must be linked to one existing employer.
One vacancy can receive several job applications.
Each job application must be linked to one existing vacancy.
Foreign keys maintain the relationships between the three database tables.
4. Entity Relationship Diagram
+-----------------------+
|       EMPLOYER        |
+-----------------------+
| PK  id                |
|     name              |
|     contact_name      |
|     email             |
|     phone             |
|     website           |
|     notes             |
+-----------------------+
           |
           | 1
           |
           | has
           |
           | many
           v
+-----------------------+
|        VACANCY        |
+-----------------------+
| PK  id                |
| FK  employer_id       |
|     title             |
|     description       |
|     location          |
|     closing_date      |
|     status            |
+-----------------------+
           |
           | 1
           |
           | receives
           |
           | many
           v
+-----------------------+
|    JOB APPLICATION   |
+-----------------------+
| PK  id                |
| FK  vacancy_id        |
|     learner_name      |
|     learner_email     |
|     application_date  |
|     status            |
|     notes             |
|     created_at        |
|     updated_at        |
+-----------------------+
Legend

PK — Primary Key: uniquely identifies each record.
FK — Foreign Key: references a record in another table.
1 — One related record.
many — Multiple related records.
5. Database Integrity Rules
The following rules help maintain accurate and consistent data:

Every record has a unique primary key.
Every vacancy must reference an existing employer.
Every job application must reference an existing vacancy.
Vacancy status must be one of the defined choices: Open, Closed, or On Hold.
Application status must be one of the defined choices: Draft, Applied, Interview, Offer, Rejected, or Withdrawn.
Email fields must contain valid email-format values.
Related employers and vacancies cannot be deleted while protected dependent records exist.
Required fields must be supplied before a valid record can be saved.
6. Implementation in Django
The data model is implemented using Django's ORM (Object-Relational Mapper). The ORM maps Python model classes to database tables and allows the application to create, retrieve, update, and delete records using Python.

For example:

# Get all vacancies belonging to an employer
employer = Employer.objects.get(id=1)
vacancies = employer.vacancies.all()

# Get all applications for a vacancy
vacancy = Vacancy.objects.get(id=1)
applications = vacancy.applications.all()
The related names vacancies and applications are available because they are defined in the foreign key fields.

After making model changes, the developer should run:

python manage.py makemigrations
python manage.py migrate
python manage.py check
7. Conclusion
The three-model structure provides a simple and maintainable database design for JEPMS. The Employer model stores organisation information, the Vacancy model stores job opportunities, and the JobApplication model tracks learner applications.

The one-to-many relationships allow multiple vacancies per employer and multiple applications per vacancy. Foreign keys help maintain referential integrity and support reliable data management throughout the application.