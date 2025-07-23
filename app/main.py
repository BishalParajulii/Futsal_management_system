from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import users, owners, bookings, auth

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI(
    title="Futsal Management System API",
    description="Book futsals, manage schedules, and more.",
    version="1.0.0"
)

# Include routers
app.include_router(users.router)
app.include_router(owners.router)
app.include_router(bookings.router)
app.include_router(auth.router)
