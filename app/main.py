from fastapi import FastAPI
from app.routers import patient, appointment, medical_record, prescription
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patient.router)
app.include_router(appointment.router)
app.include_router(medical_record.router)
app.include_router(prescription.router)
