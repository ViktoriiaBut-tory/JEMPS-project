from pydantic import BaseModel, EmailStr, Field


class EmployerCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    contact_name: str = ""
    email: EmailStr | None = None
    phone: str = ""
    website: str = ""
    notes: str = ""


class EmployerResponse(BaseModel):
    id: int
    name: str
    contact_name: str
    email: str
    phone: str
    website: str
    notes: str