from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.medical_record import MedicalRecordCreate, MedicalRecordResponse
from app.crud import medical_record as crud_medical_record
from app.dependencies import get_db

router = APIRouter(prefix="/medical_records", tags=["medical_records"])

@router.post("/", response_model=MedicalRecordResponse)
def create_medical_record(medical_record: MedicalRecordCreate, db: Session = Depends(get_db)):
    return crud_medical_record.create_medical_record(db, medical_record)

@router.get("/{record_id}", response_model=MedicalRecordResponse)
def read_medical_record(record_id: int, db: Session = Depends(get_db)):
    db_medical_record = crud_medical_record.get_medical_record(db, record_id)
    if db_medical_record is None:
        raise HTTPException(status_code=404, detail="Medical Record not found")
    return db_medical_record
