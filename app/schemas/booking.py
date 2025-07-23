from pydantic import BaseModel
from datetime import date, time

class BookingCreate(BaseModel):
    futsal_id: int
    date: date
    start_time: time
    end_time: time

class BookingOut(BookingCreate):
    id: int
    status: str

    class Config:
        orm_mode = True
