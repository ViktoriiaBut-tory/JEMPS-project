from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class JobApplicationCreate(BaseModel):
    learner_name: str = Field(min_length=1, max_length=150)
    learner_email: EmailStr
    vacancy_id: int
    application_date: date
    status: Literal[
        "Draft",
        "Applied",
        "Interview",
        "Offer",
        "Rejected",
        "Withdrawn",
    ] = "Draft"
    notes: str = ""


class JobApplicationResponse(BaseModel):
    id: int
    learner_name: str
    learner_email: str
    vacancy_id: int
    application_date: date
    status: str
    notes: str
    created_at: datetime
    updated_at: datetime