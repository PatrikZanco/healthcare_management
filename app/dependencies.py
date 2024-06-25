from app.database import SessionLocal
from app.dependencies import get_db

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
