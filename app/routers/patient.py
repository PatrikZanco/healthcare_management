from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import patient as crud_patient
from app.schemas.patient import PatientCreate, PatientResponse, PatientUpdate
from app.database import SessionLocal

router = APIRouter(prefix="/patients", tags=["patients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return crud_patient.create_patient(db, patient)

@router.get("/{patient_id}", response_model=PatientResponse)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud_patient.get_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient_update: PatientUpdate, db: Session = Depends(get_db)):
    db_patient = crud_patient.update_patient(db, patient_id, patient_update)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient
