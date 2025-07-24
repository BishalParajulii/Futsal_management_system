from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from app.db.database import Base  
from sqlalchemy.orm import relationship

# ✅ User model
class User(Base):
    __tablename__ = "users"  
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(Integer, unique=True, index=True)
    hashed_password = Column(String)
    user_type = Column(String)

    futsals = relationship("Futsal", back_populates="owner")
    bookings = relationship("Booking", back_populates="user")


# ✅ Futsal model
class Futsal(Base):  
    __tablename__ = "futsals"  

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    price_per_hour = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="futsals")
    bookings = relationship("Booking", back_populates="futsal")


# ✅ Booking model
class Booking(Base):
    __tablename__ = "bookings"  

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  
    futsal_id = Column(Integer, ForeignKey("futsals.id"))
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    status = Column(String)

    user = relationship("User", back_populates="bookings")
    futsal = relationship("Futsal", back_populates="bookings")
