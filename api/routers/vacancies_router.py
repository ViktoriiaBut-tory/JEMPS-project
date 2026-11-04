from fastapi import APIRouter, HTTPException

from applications.models import Employer, Vacancy
from api.models.vacancy_schema import VacancyCreate, VacancyResponse
from django.db.models.deletion import ProtectedError

router = APIRouter()


# get all vacancies
@router.get("/vacancies", response_model=list[VacancyResponse])
def get_vacancies():
    vacancies = Vacancy.objects.all()
    return list(vacancies)


# get one vacancy
@router.get("/vacancies/{vacancy_id}", response_model=VacancyResponse)
def get_vacancy(vacancy_id: int):
    vacancy = Vacancy.objects.filter(id=vacancy_id).first()

    if vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")

    return vacancy

# create a vacancy
# status code 201 means created

@router.post("/vacancies", response_model=VacancyResponse, status_code=201)
def create_vacancy(vacancy: VacancyCreate):
    employer_exists = Employer.objects.filter(
        id=vacancy.employer_id
    ).exists()

    if not employer_exists:
        raise HTTPException(status_code=404, detail="Employer not found")

    new_vacancy = Vacancy.objects.create(
        employer_id=vacancy.employer_id,
        title=vacancy.title,
        description=vacancy.description,
        location=vacancy.location,
        closing_date=vacancy.closing_date,
        status=vacancy.status,
    )

    return new_vacancy

# update a vacancy
@router.put("/vacancies/{vacancy_id}", response_model=VacancyResponse)
def update_vacancy(vacancy_id: int, vacancy: VacancyCreate):
    existing_vacancy = Vacancy.objects.filter(id=vacancy_id).first()

    if existing_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")

    employer_exists = Employer.objects.filter(
        id=vacancy.employer_id
    ).exists()

    if not employer_exists:
        raise HTTPException(status_code=404, detail="Employer not found")

    existing_vacancy.employer_id = vacancy.employer_id
    existing_vacancy.title = vacancy.title
    existing_vacancy.description = vacancy.description
    existing_vacancy.location = vacancy.location
    existing_vacancy.closing_date = vacancy.closing_date
    existing_vacancy.status = vacancy.status
    existing_vacancy.save()

    return existing_vacancy

# delete a vacancy
@router.delete("/vacancies/{vacancy_id}")
def delete_vacancy(vacancy_id: int):
    vacancy = Vacancy.objects.filter(id=vacancy_id).first()

    if vacancy is None:
        raise HTTPException(
            status_code=404,
            detail="Vacancy not found, try again"
        )

    try:
        vacancy.delete()
    except ProtectedError:
        raise HTTPException(
            status_code=409,
            detail="Cannot delete vacancy with existing applications"
        ) from None

    return {
        "message": "Vacancy deleted successfully",
        "id": vacancy_id
    }