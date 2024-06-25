from datetime import datetime
from pydantic import BaseModel

class AppointmentBase(BaseModel):
    patient_id: int
    date_time: datetime
    reason: str

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
