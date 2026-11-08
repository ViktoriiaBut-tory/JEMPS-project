import pytest
from fastapi.testclient import TestClient


from api.main import app
from applications.models import Employer

client = TestClient(app)


@pytest.mark.django_db(transaction=True)
def test_get_all_employers():
    Employer.objects.create(
        name="Test Company",
        email="test@example.com"
    )
    response = client.get("/employers")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Test Company"

    
@pytest.mark.django_db(transaction=True)
def test_get_employer_by_id():
    employer = Employer.objects.create(
        name="ABCD Company",
        email="abcd@example.com"
    )
    response = client.get(f"/employers/{employer.id}")
    
    assert response.status_code == 200
    assert response.json()["name"] == "ABCD Company"
    assert response.json()["id"] == employer.id
    
    
@pytest.mark.django_db(transaction=True)
def test_get_employer_not_found():
    response = client.get("/employers/999")
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Employer not found"

    
@pytest.mark.django_db(transaction=True)
def test_create_employer():
    employer_data = {
        "name": "New Test Company",
        "contact_name": "John Smith",
        "email": "john@example.com",
        "phone": "0123456789",
        "website": "https://example.com",
        "notes": "Created using FastAPI test"       
    }   
    response = client.post("/employers", json=employer_data)
    
    assert response.status_code == 201
    assert response.json()["name"] == "New Test Company"
    assert response.json()["email"] == "john@example.com"
    assert "id" in response.json()
    