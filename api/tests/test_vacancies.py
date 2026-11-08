import pytest
from fastapi.testclient import TestClient
from api.main import app 
from applications.models import Employer, Vacancy

client = TestClient(app)

@pytest.mark.django_db(transaction=True)
def test_get_all_vacancies():
    employer = Employer.objects.create(
        name="Test IT Company",
        email="company@example.com"        
    )
    Vacancy.objects.create(
        employer=employer,
        title="Junior Python Developer",
        description="Python and Django development",
        location="York",
        status="Open"        
    )
    response = client.get("/vacancies")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Junior Python Developer"
    assert response.json()[0]["status"] == "Open"
    assert response.json()[0]["employer_id"] == employer.id
    
    
@pytest.mark.django_db(transaction=True)
def test_create_vacancy():
    employer = Employer.objects.create(
        name="ABCD Company",
        email="abcd@example.com"
    )
    vacancy_data = {
        "employer_id": employer.id,
        "title": "Junior Software Developer",
        "description": "Python and Django",
        "location": "York",
        "closing_date": "2026-12-15",
        "status": "Open"
    }
    response = client.post("/vacancies", json=vacancy_data)

    assert response.status_code == 201
    assert response.json()["title"] == "Junior Software Developer"
    assert response.json()["employer_id"] == employer.id
    assert response.json()["status"] == "Open"
    assert "id" in response.json()
    
@pytest.mark.django_db(transaction=True)
def test_create_vacancy_employer_not_found():
    vacancy_data = {
        "employer_id": 999,
        "title": "Junior Python Developer",
        "description": "Python development",
        "location": "Leeds",
        "closing_date": None,
        "status": "Open"
    }
    response = client.post("/vacancies", json=vacancy_data)

    assert response.status_code == 404
    assert response.json()["detail"] == "Employer not found"