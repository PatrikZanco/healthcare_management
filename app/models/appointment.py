from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from .patient import Patient  # Import from sibling module to avoid circular import

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    date_time = Column(DateTime, default=datetime.utcnow)
    reason = Column(String)
    patient = relationship("Patient")
