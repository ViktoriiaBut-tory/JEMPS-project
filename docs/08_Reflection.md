# 08 – Project Reflection: What I Learned

## 1. Introduction

During this project, I learned how to plan, develop, test and deploy a web application using Python and Django.

JEPMS was a good opportunity for me to practise the skills I learned during my IT Skills Bootcamp.

Some tasks were difficult because I am still learning, but I gained more confidence by completing them step by step.

## 2. Project Planning

I learned how to understand a business problem and identify the main requirements of an application.

I practised writing a project brief, defining user needs and creating acceptance criteria.

I also used GitHub Projects Kanban to organise my work into To Do, In Progress and Done.

This helped me understand how developers can plan and track their tasks.

## 3. Django Development

I learned how to create a Django project and application, organise files and connect different parts of the system.

I practised working with models, views, templates, forms and URLs.

I also learned how to use Django migrations to create and update database tables.

## 4. Database Relationships

I learned how to create relationships between database models using ForeignKey.

In JEPMS, I connected employers to vacancies and vacancies to job applications.

This helped me understand how related information can be stored and managed in a database.

## 5. Forms and CRUD Operations

I learned how to use Django ModelForms to collect and validate user information.

I practised creating CRUD functionality:

- Create new records.
- Read and display information.
- Update existing records.
- Delete records.

I also learned how to use function-based views and class-based views.

## 6. Authentication and Security

I learned how Django's authentication system works and how to protect pages using login requirements.

I practised using `login_required`, `LoginRequiredMixin` and CSRF tokens.

I also learned why secret keys and environment variables should not be uploaded to GitHub.

## 7. Testing and Debugging

I learned how to write automated tests using Django TestCase.

I practised testing models, forms and views.

During testing, I had to find and correct several errors, including indentation problems, incorrect HTTP responses and form validation issues.

At the end of the project, all 18 automated tests passed.

This helped me understand why testing is important in software development.

## 8. Git and GitHub

I gained more experience using Git commands to save my work.

I practised creating commits, pushing changes to GitHub and checking the repository status.

I learned how GitHub can help developers manage project versions and keep their code organised.

## 9. Deployment to PythonAnywhere

I learned how to deploy a Django application to PythonAnywhere.

I practised cloning a GitHub repository, creating a virtual environment, installing dependencies and running database migrations.

I also learned how to configure environment variables, WSGI and the web application settings.

During deployment, I received a Bad Request (400) error. I investigated the problem and found an incorrect domain name in `ALLOWED_HOSTS`.

After correcting the setting, the website worked successfully.

This experience helped me understand how to solve problems when an application works locally but has errors on a server.

## 10. Final Reflection

This project helped me bring together many skills from my course.

Before starting JEPMS, I had practised Django in smaller exercises. In this project, I used these skills together to build a complete application.

I learned that software development involves more than writing code. It also includes planning, testing, debugging, security, documentation and deployment.

I am still a beginner, and I sometimes need guidance to understand errors and new concepts. However, completing this project helped me feel more confident working with Python and Django.

I am pleased that I completed the project, passed all 18 automated tests and successfully deployed the application online.