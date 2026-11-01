from django.test import TestCase
from .models import Employer, Vacancy, JobApplication
from .forms import EmployerForm, VacancyForm, JobApplicationForm
from django.contrib.auth import get_user_model

# Create your tests here.
class EmployerModelTest(TestCase):
    def test_create_employer(self):
        employer = Employer.objects.create(
            name="Tech Solutions Ltd",
            contact_name="John Smith",
            email="john@example.com",
    ) 
        self.assertEqual(employer.name,"Tech Solutions Ltd")
        self.assertEqual(employer.contact_name,"John Smith")
        self.assertEqual(employer.email,"john@example.com")
        

class VacancyModelTest(TestCase):
    def test_create_vacancy(self):
        employer = Employer.objects.create(
            name="Tech Solutions Ltd"
        )
        vacancy = Vacancy.objects.create(
            employer = employer,
            title = "Python Developer",
            description = "Develop Python applications",
            location = "York",
            status = "open",
        )
        self.assertEqual(vacancy.title,"Python Developer")
        self.assertEqual(vacancy.employer, employer)
        self.assertEqual(vacancy.status, "open")
        
class JobApplicationModelTest(TestCase):
    def test_create_application(self):
        employer = Employer.objects.create(
             name="Tech Solutions Ltd"
        )
        vacancy = Vacancy.objects.create(
            employer = employer,
            title = "Python Developer",
            description = "Develop Python applications",
            location = "York",
            status = "open",
        )
        application = JobApplication.objects.create(
            learner_name = "Anna",
            learner_email = "anna@rrrr.com",
            vacancy = vacancy,
            application_date = "2026-11-01",
            status = "Applied",
        )        
        self.assertEqual(application.learner_name,"Anna" )
        self.assertEqual(application.learner_email, "anna@rrrr.com")
        self.assertEqual(application.vacancy, vacancy)
        self.assertEqual(application.status, "Applied")
        
class EmployerFormTest(TestCase):
    def test_valid_emloyer_form(self):
        form_data = {
            "name": "Tech Solutions Ltd",
            "contact_name": "John Smith",
            "email": "john@example.com",
            "phone": "123456789",
            "website": "https://example.com",
            "notes": "IT company",
        }
        form = EmployerForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_employer_email(self):
        form_data = {
            "name": "Tech Solutions Ltd",
            "contact_name": "John Smith",
            "email": "incorrect-email",
            "phone": "123456789",
            "website": "https://example.com",
            "notes": "IT company",
        }
        form = EmployerForm(data = form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
        
class VacancyFormTest(TestCase):
    def test_valid_vacancy_form(self):
        employer = Employer.objects.create(
           name="Tech Solutions Ltd" 
        )
        form_data = {
            "employer": employer.id,
            "title": "Python Developer",
            "description":"Develop Python applications",
            "closing_date": "2026-12-01",
            "location": "York",
            "status": "Open",
        }
        form = VacancyForm(data =form_data)
        self.assertTrue(form.is_valid(), form.errors)
        
class JobApplicationFormTest(TestCase):
    def test_valid_application_form(self):
        employer = Employer.objects.create(
            name="Tech Solutions Ltd" 
        )
        vacancy = Vacancy.objects.create(
            employer =employer,
            title = "Python Developer",
            description = "Develop Python applications",
            location = "York",
            status = "open",
        )
        form_data = {
            "learner_name": "Anna",
            "learner_email": "anna@rrrr.com",
            "vacancy": vacancy.id,
            "application_date": "2026-11-01",
            "status": "Applied",
            "notes": "First application",
        }
        form = JobApplicationForm(data = form_data)
        self.assertTrue = (form.is_valid(), form.errors)
        
    def test_invalid_application_email(self):
        employer = Employer.objects.create(
            name="Tech Solutions Ltd"
        )
        vacancy = Vacancy.objects.create(
            employer=employer,
            title="Python Developer",
            description="Develop Python applications",
            location="York",
            status="Open",
        )
        form_data = {
            "learner_name": "Anna",
            "learner_email": "incorrect-email",
            "vacancy": vacancy.id,
            "application_date": "2026-11-01",
            "status": "Applied",
            "notes": "First application",
        }

        form = JobApplicationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("learner_email", form.errors)
        
class EmployerViewTest(TestCase):

    def test_employer_list_requires_login(self):
        response = self.client.get("/employers/")
        self.assertEqual(response.status_code, 302)

    def test_employer_list_with_login(self):
        from django.contrib.auth import get_user_model

        User = get_user_model()

        user = User.objects.create_user(
            username="testuser",
            password="testpass12345"
        )
        self.assertTrue(user.check_password("testpass12345"))
        self.client.force_login(user)
        response = self.client.get("/employers/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employers/list.html")
        
    def test_create_employer(self):
        User = get_user_model()

        user = User.objects.create_user(
            username="testuser",
            password="testpass12345"
        )

        self.client.force_login(user)

        response = self.client.post("/employers/add/", {
            "name": "New IT Company",
            "contact_name": "John Smith",
            "email": "john@example.com",
            "phone": "123456789",
            "website": "https://example.com",
            "notes": "Test employer",
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Employer.objects.filter(name="New IT Company").exists()
        )
        
    def test_update_employer(self):    
        User = get_user_model()   

        user = User.objects.create_user(
            username="testuser",
            password="testpass12345"
        )
        self.client.force_login(user)

        employer = Employer.objects.create(
            name="Old Company",
            email="old@example.com"
        )
        response = self.client.post(
            f"/employers/{employer.pk}/edit/",
            {
                "name": "Updated Company",
                "contact_name": "John Smith",
                "email": "new@example.com",
                "phone": "123456789",
                "website": "https://example.com",
                "notes": "Updated employer",
            }
        )
        employer.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(employer.name, "Updated Company")
        self.assertEqual(employer.email, "new@example.com")
        
    def test_delete_employer(self):  
        User = get_user_model()

        user = User.objects.create_user(
            username="testuser",
            password="testpass12345"
        )
        self.client.force_login(user)
        employer = Employer.objects.create(
            name="Test Company",
            email="test@example.com"
        )
        response = self.client.post(
            f"/employers/{employer.pk}/delete/"
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Employer.objects.filter(pk=employer.pk).exists()
        )
        
class VacancyViewTest(TestCase):
    def test_vacancy_list_with_login(self):
        from django.contrib.auth import get_user_model

        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            password="testpass12345"
        )

        self.client.force_login(user)

        response = self.client.get("/vacancies/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "vacancies/list.html")
        
    def test_vacancy_list_requires_login(self):
        response = self.client.get("/vacancies/")
        
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)


class JobApplicationViewTest(TestCase):

    def test_application_list_with_login(self):
        from django.contrib.auth import get_user_model

        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            password="testpass12345"
        )

        self.client.force_login(user)
        response = self.client.get("/applications/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "applications/list.html")
        
    def test_application_list_requires_login(self):
        response = self.client.get("/applications/")
        
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)
        
    def test_create_application(self):
        User = get_user_model()

        user = User.objects.create_user(
            username="testuser",
            password="testpass12345"
        )
        self.client.force_login(user)
        employer = Employer.objects.create(
            name="Tech Solutions Ltd"
        )
        vacancy = Vacancy.objects.create(
            employer=employer,
            title="Python Developer",
            description="Develop Python applications",
            location="York",
            status="Open",
        )
        response = self.client.post(
            "/applications/add/",
            {
                "learner_name": "Anna Smith",
                "learner_email": "anna@example.com",
                "vacancy": vacancy.pk,
                "application_date": "2026-11-01",
                "status": "Applied",
                "notes": "Test application",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            JobApplication.objects.filter(
                learner_name="Anna Smith"
            ).exists()
        )