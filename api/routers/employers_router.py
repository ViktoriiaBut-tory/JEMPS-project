from fastapi import APIRouter, HTTPException
from applications.models import Employer
from api.models.employer_schema import EmployerCreate, EmployerResponse

router = APIRouter()

@router.get("/employers")
def get_employers():
    employers = Employer.objects.all()
    return [
        {
            "id": employer.id,
            "name": employer.name,
            "contact_name": employer.contact_name,
            "email": employer.email,
            "phone": employer.phone,
            "website": employer.website,
            "notes": employer.notes,
        }
        for employer in employers
    ]
    
@router.get("/employers/{employer_id}")
def get_employer(employer_id: int):
    employer = Employer.objects.filter(id=employer_id).first()

    if employer is None:
        raise HTTPException(status_code=404, detail="Employer not found")

    return {
        "id": employer.id,
        "name": employer.name,
        "contact_name": employer.contact_name,
        "email": employer.email,
        "phone": employer.phone,
        "website": employer.website,
        "notes": employer.notes,
    }
    
# create an employer
# status code 201 means created

@router.post(
    "/employers",
    response_model=EmployerResponse,
    status_code=201
)
def create_employer(employer: EmployerCreate):
    new_employer = Employer.objects.create(
        name=employer.name,
        contact_name=employer.contact_name,
        email=str(employer.email or ""),
        phone=employer.phone,
        website=employer.website,
        notes=employer.notes,
    )

    return new_employer

# update an employer
@router.put("/employers/{employer_id}", response_model=EmployerResponse)
def update_employer(employer_id: int, employer: EmployerCreate):
    existing_employer = Employer.objects.filter(id=employer_id).first()

    if existing_employer is None:
        raise HTTPException(status_code=404, detail="Employer not found")

    existing_employer.name = employer.name
    existing_employer.contact_name = employer.contact_name
    existing_employer.email = str(employer.email or "")
    existing_employer.phone = employer.phone
    existing_employer.website = employer.website
    existing_employer.notes = employer.notes

    existing_employer.save()

    return existing_employer

# delete an employer
@router.delete("/employers/{employer_id}")
def delete_employer(employer_id: int):
    employer = Employer.objects.filter(id=employer_id).first()

    if employer is None:
        raise HTTPException(status_code=404, detail="Employer not found")

    employer.delete()

    return {"message": "Employer deleted successfully"}