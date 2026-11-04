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