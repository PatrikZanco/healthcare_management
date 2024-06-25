from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    email: str
    age: int
    address: str

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int

    class Config:
        orm_mode = True
