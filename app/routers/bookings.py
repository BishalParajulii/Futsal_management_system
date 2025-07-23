from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.booking import BookingCreate, BookingOut
from app.crud import booking as booking_crud
from app.db.database import SessionLocal
from typing import List

router = APIRouter(prefix="/bookings", tags=["Bookings"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=BookingOut)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    # Placeholder user_id = 2 (replace later with actual authenticated user)
    return booking_crud.create_booking(db, booking, user_id=2)

@router.get("/owner", response_model=List[BookingOut])
def get_owner_bookings(db: Session = Depends(get_db)):
    return booking_crud.get_bookings_for_owner(db, owner_id=1)  # placeholder owner_id

@router.patch("/{booking_id}/status")
def update_booking_status(booking_id: int, status: str, db: Session = Depends(get_db)):
    return booking_crud.update_booking_status(db, booking_id, status)
