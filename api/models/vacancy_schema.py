from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class VacancyCreate(BaseModel):
    employer_id: int
    title: str = Field(min_length=1, max_length=150)
    description: str = ""
    location: str = ""
    closing_date: date | None = None
    status: Literal["Open", "Closed", "On hold"] = "Open"


class VacancyResponse(BaseModel):
    id: int
    employer_id: int
    title: str
    description: str
    location: str
    closing_date: date | None
    status: str