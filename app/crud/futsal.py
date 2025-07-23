from sqlalchemy.orm import Session
from app import schemas
from app.db import models

def create_futsal(db: Session, futsal: schemas.futsal.FutsalCreate, owner_id: int):
    db_futsal = models.Futsal(**futsal.dict(), owner_id=owner_id)
    db.add(db_futsal)
    db.commit()
    db.refresh(db_futsal)
    return db_futsal

def get_all_futsals(db: Session):
    return db.query(models.Futsal).all()
