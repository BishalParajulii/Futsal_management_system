from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.futsal import FutsalCreate, FutsalOut
from app.crud import futsal as futsal_crud
from app.db.database import SessionLocal

router = APIRouter(prefix="/owners", tags=["Futsal Owners"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add-futsal", response_model=FutsalOut)
def add_futsal(futsal: FutsalCreate, db: Session = Depends(get_db)):
    # Placeholder owner_id = 1 for now (replace later with actual authenticated user)
    return futsal_crud.create_futsal(db, futsal, owner_id=1)
