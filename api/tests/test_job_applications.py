import pytest
from datetime import date
from fastapi.testclient import TestClient
from api.main import app
from applications.models import Employer, Vacancy, JobApplication

client = TestClient(app)

@pytest.mark.django_db(transaction=True)
def test_get_all_applications():
    employer = Employer.objects.create(
        name="Test Company",
        email="test@example.com"    
    )
    vacancy = Vacancy.objects.create(
        employer=employer,
        title="Junior Python Developer",
        location="York",
        status="Open"
    )
    
    JobApplication.objects.create(
        learner_name="Anna",
        learner_email="anna@example.com",
        vacancy=vacancy,
        application_date=date(2026, 11, 8),
        status="Applied",
        notes="Test application"
    )
    response = client.get("/job-applications")
    
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["learner_name"] == "Anna"
    assert response.json()[0]["status"] == "Applied"
    assert response.json()[0]["vacancy_id"] == vacancy.id
    
    
@pytest.mark.django_db(transaction=True)
def test_create_applications():
    employer = Employer.objects.create(
        name="ABCD Company",
        email="abcd@example.com"
    )
    vacancy = Vacancy.objects.create(
        employer=employer,
        title="Junior Software Developer",
        location="Leeds",
        status="Open"
    )
    application_data = {
        "learner_name": "John Smith",
        "learner_email": "john@example.com",
        "vacancy_id": vacancy.id,
        "application_date": "2026-11-08",
        "status": "Applied",
        "notes": "Created using FastAPI test"
    }
    response = client.post("/job-applications", json=application_data)
    
    assert response.status_code == 201
    assert response.json()["learner_name"] == "John Smith"
    assert response.json()["vacancy_id"] == vacancy.id
    assert response.json()["status"] == "Applied"
    assert "id" in response.json()
    

@pytest.mark.django_db(transaction=True) 
def test_update_application():
    employer = Employer.objects.create(
        name="Test Company"
    )
    vacancy = Vacancy.objects.create(
        employer=employer,
        title="Junior Python Developer",
        location="York",
        status="Open"
    )
    application = JobApplication.objects.create(
        learner_name="Anna",
        learner_email="anna@example.com",
        vacancy=vacancy,
        application_date=date(2026, 11, 8),
        status="Applied" 
    )
    updated_data = {
        "learner_name": "Anna Smith",
        "learner_email": "anna@example.com",
        "vacancy_id": vacancy.id,
        "application_date": "2026-11-08",
        "status": "Interview",
        "notes": "Invited to interview"
    }
    response = client.put(f"/job-applications/{application.id}", json=updated_data)
    
    assert response.status_code == 200
    assert response.json()["status"] == "Interview"
    assert response.json()["notes"] == "Invited to interview"
    assert response.json()["id"] == application.id
    
    application.refresh_from_db()
    assert application.status == "Interview"
    
    
@pytest.mark.django_db(transaction=True)
def test_delete_application():
    employer = Employer.objects.create(
        name="Test Company"
    )

    vacancy = Vacancy.objects.create(
        employer=employer,
        title="Junior Python Developer",
        location="York",
        status="Open"
    )
    application = JobApplication.objects.create(
        learner_name="John Smith",
        learner_email="john@example.com",
        vacancy=vacancy,
        application_date=date(2026, 11, 8),
        status="Applied"
    )
    application_id = application.id

    response = client.delete(
        f"/job-applications/{application_id}"
    )

    assert response.status_code == 200
    assert response.json()["message"] == ("Job application deleted successfully")
    assert response.json()["id"] == application_id

    assert not JobApplication.objects.filter(id=application_id).exists()
        
    
    