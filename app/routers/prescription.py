from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.prescription import PrescriptionCreate, PrescriptionResponse
from app.crud.prescription import create_prescription, get_prescription
from app.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=PrescriptionResponse)
def create_new_prescription(prescription: PrescriptionCreate, db: Session = Depends(get_db)):
    db_prescription = create_prescription(db, prescription)
    return db_prescription

@router.get("/{prescription_id}", response_model=PrescriptionResponse)
def read_prescription(prescription_id: int, db: Session = Depends(get_db)):
    db_prescription = get_prescription(db, prescription_id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription
