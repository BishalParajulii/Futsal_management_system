from sqlalchemy.orm import Session
from app import schemas
from app.db import models

def create_booking(db: Session, booking: schemas.booking.BookingCreate, user_id: int):
    db_booking = models.Booking(**booking.dict(), user_id=user_id)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_bookings_for_owner(db: Session, owner_id: int):
    return db.query(models.Booking).join(models.Futsal).filter(models.Futsal.owner_id == owner_id).all()

def update_booking_status(db: Session, booking_id: int, status: str):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if booking:
        booking.status = status
        db.commit()
        db.refresh(booking)
    return booking
