from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    email: str
    age: int

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None

class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True
