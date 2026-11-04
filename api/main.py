import os

import django
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JEPMSproject.settings")
django.setup()

from api.routers import employers_router,vacancies_router,job_applications_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to JEPMS FastAPI"}


app.include_router(employers_router.router)
app.include_router(vacancies_router.router)
app.include_router(job_applications_router.router)