from fastapi import APIRouter, HTTPException

from applications.models import JobApplication, Vacancy
from api.models.job_application_schema import JobApplicationCreate, JobApplicationResponse



router = APIRouter()


# get all job applications
@router.get(
    "/job-applications",
    response_model=list[JobApplicationResponse]
)
def get_all_applications():
    applications = JobApplication.objects.all()
    return list(applications)


# get one job application
@router.get(
    "/job-applications/{application_id}",
    response_model=JobApplicationResponse
)
def get_application(application_id: int):
    application = JobApplication.objects.filter(
        id=application_id
    ).first()

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Job application not found, try again"
        )

    return application


# create a job application
# status code 201 means created

@router.post(
    "/job-applications",
    response_model=JobApplicationResponse,
    status_code=201
)
def create_application(application: JobApplicationCreate):
    vacancy_exists = Vacancy.objects.filter(
        id=application.vacancy_id
    ).exists()

    if not vacancy_exists:
        raise HTTPException(
            status_code=404,
            detail="Vacancy not found"
        )

    new_application = JobApplication.objects.create(
        learner_name=application.learner_name,
        learner_email=str(application.learner_email),
        vacancy_id=application.vacancy_id,
        application_date=application.application_date,
        status=application.status,
        notes=application.notes,
    )

    return new_application

# update a job application
@router.put(
    "/job-applications/{application_id}",
    response_model=JobApplicationResponse
)
def update_application(application_id: int, application: JobApplicationCreate):
    existing_application = JobApplication.objects.filter(
        id=application_id
    ).first()

    if existing_application is None:
        raise HTTPException(
            status_code=404,
            detail="Job application not found, try again"
        )

    vacancy_exists = Vacancy.objects.filter(
        id=application.vacancy_id
    ).exists()

    if not vacancy_exists:
        raise HTTPException(
            status_code=404,
            detail="Vacancy not found"
        )

    existing_application.learner_name = application.learner_name
    existing_application.learner_email = str(application.learner_email)
    existing_application.vacancy_id = application.vacancy_id
    existing_application.application_date = application.application_date
    existing_application.status = application.status
    existing_application.notes = application.notes

    existing_application.save()

    return existing_application


# delete a job application
@router.delete("/job-applications/{application_id}")
def delete_application(application_id: int):
    application = JobApplication.objects.filter(
        id=application_id
    ).first()

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Job application not found, try again"
        )

    application.delete()

    return {
        "message": "Job application deleted successfully",
        "id": application_id
    }